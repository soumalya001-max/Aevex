"""Legacy blocking listener.

Phase 5 uses voice/background_listener.py for continuous wake + command
recording.

Kept for backward compatibility.
"""

import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...\n")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text
    except Exception:
        return ""

