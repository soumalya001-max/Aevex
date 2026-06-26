import queue
import threading
import time
import sys
from typing import Optional, Tuple


import speech_recognition as sr


from voice.mic_lock import MIC_LOCK
from voice.voice_constants import (
    WAKE_POLL_INTERVAL_SEC,
    MAX_RECORDING_SEC,
    SILENCE_TIMEOUT_SEC,
)


class BackgroundVoiceListener:


    """Continuous background listener.

    Uses speech_recognition to capture chunks and performs two-stage logic:
    - wake word detection by recognizing short chunks and checking for wake phrases
    - command recording after wake word, collecting speech until silence timeout or max duration

    This is Windows-first and aims to keep CPU/RAM low by relying on the
    library's audio pipeline + short polling intervals.
    """

    def __init__(self, wake_words, on_wake_callback):
        self._wake_words = [w.lower() for w in wake_words]
        self._on_wake = on_wake_callback

        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()

        self._last_failure_ts = 0.0

    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop_event.set()

    @staticmethod
    def _normalize_text(text: str) -> str:
        return " ".join((text or "").strip().lower().split())

    def _recognize_audio(self, audio) -> str:
        # External speech_recognition provider call; may raise.
        return self._recognizer.recognize_google(audio)

    def _get_short_chunk(self) -> Tuple[Optional[object], float]:
        """Capture a short audio chunk.

        Returns: (audio, duration_seconds)
        """
        start = time.time()
        with MIC_LOCK:
            with self._microphone as source:
                # Keep ambient adjustment minimal to reduce startup latency.
                try:
                    self._recognizer.adjust_for_ambient_noise(source, duration=0.5)
                except Exception:
                    # Ambient adjustment should never kill the listener.
                    pass
                audio = self._recognizer.listen(
                    source,
                    timeout=1,
                    phrase_time_limit=1,
                )
        return audio, max(0.001, time.time() - start)

    def _run(self):
        # Warm-up once to reduce first-latency.
        try:
            with MIC_LOCK:
                with self._microphone as source:
                    try:
                        self._recognizer.adjust_for_ambient_noise(source, duration=0.7)
                    except Exception:
                        pass
        except Exception:
            pass

        iterations = 0
        while not self._stop_event.is_set():
            iterations += 1
            if iterations > 1000000:
                # Safety: avoid accidental infinite loop if clocking breaks.
                return

            try:
                audio, _dur = self._get_short_chunk()
                if self._stop_event.is_set():
                    return

                if audio is None:
                    time.sleep(WAKE_POLL_INTERVAL_SEC)
                    continue

                text = ""
                try:
                    text = self._recognize_audio(audio)
                except Exception:
                    text = ""

                norm = self._normalize_text(text)
                if not norm:
                    time.sleep(WAKE_POLL_INTERVAL_SEC)
                    continue

                # Wake word match
                for w in self._wake_words:
                    if w in norm:
                        # Callback to main voice pipeline.
                        self._on_wake()
                        break

                time.sleep(WAKE_POLL_INTERVAL_SEC)

            except sr.WaitTimeoutError:
                # Silence -> not an error. Keep the background loop alive.
                continue

            except Exception:
                # Unexpected failure: log one concise (throttled) message and keep listening.
                now = time.time()
                if now - self._last_failure_ts >= 5.0:
                    self._last_failure_ts = now
                    print("[Voice mode] Listener error:", str(sys.exc_info()[1]) if sys.exc_info()[1] else "unknown")
                time.sleep(0.5)



    def wait_for_command(self, stop_event: threading.Event) -> str:
        """After wake word detection, record until silence timeout or max duration.

        Returns recognized text (may be empty on failure).
        """
        start_time = time.time()
        collected = []

        while not stop_event.is_set() and (time.time() - start_time) < MAX_RECORDING_SEC:
            # Use short chunking and stop when consecutive failures/empty => silence gate.
            try:
                with MIC_LOCK:
                    with self._microphone as source:
                        try:
                            # Keep ambient adjust short to reduce latency.
                            self._recognizer.adjust_for_ambient_noise(source, duration=0.3)
                        except Exception:
                            pass
                        audio = self._recognizer.listen(
                            source,
                            timeout=2,
                            phrase_time_limit=1,
                        )
                if audio is None:
                    continue

                try:
                    text = self._recognize_audio(audio)
                except Exception:
                    text = ""

                if text:
                    collected.append(text)
                    last_speech = time.time()
                else:
                    # If no speech detected, check silence timeout.
                    if collected:
                        # If already have something, silence gate is based on elapsed since last recognized chunk.
                        # Estimate last_speech using last successful collection timestamp.
                        # Simpler: treat time since start as silence gate when no new tokens arrive.
                        if (time.time() - last_speech) >= SILENCE_TIMEOUT_SEC:
                            break
                    else:
                        # No content yet, keep listening a bit.
                        time.sleep(0.1)

                # Maintain silence timeout even if recognition returns empty repeatedly.
                if collected and (time.time() - last_speech) >= SILENCE_TIMEOUT_SEC:
                    break

            except sr.WaitTimeoutError:
                # Silence -> keep command recording alive.
                continue

            except Exception:
                now = time.time()
                if now - self._last_failure_ts >= 5.0:
                    self._last_failure_ts = now
                    print("[Voice mode] Listener error:", str(sys.exc_info()[1]) if sys.exc_info()[1] else "unknown")
                time.sleep(0.3)


        return self._normalize_text(" ".join(collected)).strip()

