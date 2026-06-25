from voice.listen import listen
from voice.speak import speak

from core.router import ask_ai

from memory.memory_manager import (
    add_conversation
)

from memory.semantic_memory import (
    update_semantic_memory
)


def start_voice_mode():

    print("\nVOICE MODE STARTED\n")

    while True:

        user_input = listen()

        if user_input == "":

            continue

        if user_input.lower() == "exit":

            speak(

                "Goodbye"

            )

            break

        response = ask_ai(

            user_input

        )

        add_conversation(

            user_input,

            response

        )

        update_semantic_memory(

            user_input

        )

        print()

        print(

            "AEVEX:",

            response

        )

        print()

        speak(

            response

        )