from core.router import ask_ai

from agents.planner_agent import create_plan

print(
    create_plan(
        input("Test Prompt: ")
    )
)

from memory.memory_manager import (
    add_conversation
)

from memory.semantic_memory import (
    update_semantic_memory
)

from memory.identity_engine import (
    update_identity
)

from voice.voice_mode import (
    start_voice_mode
)

print("=== AEVEX V1 ===")

print("1. Text Mode")
print("2. Voice Mode")

choice = input(
    "\nSelect mode: "
)

# ==========================
# VOICE MODE
# ==========================

if choice == "2":

    start_voice_mode()

# ==========================
# TEXT MODE
# ==========================

else:

    while True:

        user_input = input(
            "\nYou: "
        )

        if user_input.lower() == "exit":

            print(
                "\nAEVEX: Goodbye."
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

        update_identity(
            user_input
        )

        print()

        print(
            "AEVEX:",
            response
        )

        print()