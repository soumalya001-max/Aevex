import asyncio
import os
import threading
import time

import edge_tts
import pygame

from language.language_detector import detect_language

# Avoid reinitializing mixer and busy-waiting; keep this lightweight.
_MIXER_LOCK = threading.Lock()
_MIXER_INITIALIZED = False


async def generate_voice(text: str, out_path: str):

    language = detect_language(text)

    voice_name = "en-US-ChristopherNeural"

    if language == "hi":
        voice_name = "hi-IN-MadhurNeural"
    elif language == "bn":
        voice_name = "bn-BD-NabanitaNeural"

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice_name,
    )

    await communicate.save(out_path)


def speak(text: str, max_wait_sec: float = 30.0):
    """Speak using edge-tts -> pygame.

    max_wait_sec prevents infinite hangs.
    """

    if not text:
        return


    out_path = "voice.mp3"

    # Generate mp3 (async)
    asyncio.run(generate_voice(text, out_path))

    global _MIXER_INITIALIZED

    with _MIXER_LOCK:
        if not _MIXER_INITIALIZED:
            pygame.mixer.init()
            _MIXER_INITIALIZED = True

        pygame.mixer.music.load(out_path)
        pygame.mixer.music.play()

        start = time.time()
        while pygame.mixer.music.get_busy():
            if (time.time() - start) > max_wait_sec:
                break
            time.sleep(0.05)

    # Cleanup file best-effort
    try:
        if os.path.exists(out_path):
            pass
    except Exception:
        pass

