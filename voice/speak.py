import asyncio
import edge_tts
import pygame

from language.language_detector import detect_language


async def generate_voice(text):

    language = detect_language(text)

    voice_name = "en-US-ChristopherNeural"

    if language == "hi":

        voice_name = "hi-IN-MadhurNeural"

    elif language == "bn":

        voice_name = "bn-BD-NabanitaNeural"

    communicate = edge_tts.Communicate(

        text=text,
        voice=voice_name

    )

    await communicate.save("voice.mp3")


def speak(text):

    asyncio.run(

        generate_voice(text)

    )

    pygame.mixer.init()

    pygame.mixer.music.load(

        "voice.mp3"

    )

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        pass