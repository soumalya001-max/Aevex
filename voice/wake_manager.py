import threading

from voice.voice_constants import WAKE_WORDS
from voice.background_listener import BackgroundVoiceListener


class WakeManager:
    def __init__(self, on_wake):
        self._on_wake = on_wake
        self._wake_event = threading.Event()
        self._listening = False

        def _wake_cb():
            # Set event; handled by main voice mode thread.
            if not self._wake_event.is_set():
                self._wake_event.set()
            self._on_wake()

        self._bg = BackgroundVoiceListener(
            wake_words=WAKE_WORDS,
            on_wake_callback=_wake_cb,
        )

    def start(self):
        self._listening = True
        self._bg.start()

    def stop(self):
        self._listening = False
        self._bg.stop()

    def wait_for_wake(self, timeout=None) -> bool:
        return self._wake_event.wait(timeout=timeout)

    def clear_wake(self):
        self._wake_event.clear()

    def is_running(self):
        return self._listening

    def wait_for_command_text(self, stop_event: threading.Event) -> str:
        return self._bg.wait_for_command(stop_event)

