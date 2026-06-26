# ==========================
# AEVEX - INSTANT STARTUP
# ==========================

print("=== AEVEX V1 ===")

print("1. Text Mode")
print("2. Voice Mode")

choice = input("\nSelect mode: ")

# ==========================
# VOICE MODE
# ==========================

if choice == "2":
    from voice.voice_mode import start_voice_mode

    start_voice_mode()

    # Voice mode runs continuously and will only return when explicitly exited.

# ==========================
# TEXT MODE
# ==========================

else:
    from core.router import ask_ai

    from memory.memory_manager import add_conversation

    from memory.semantic_memory import update_semantic_memory

    from memory.identity_engine import update_identity

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("\nAEVEX: Goodbye.")
            break

        response = ask_ai(user_input)

        add_conversation(user_input, response)

        update_semantic_memory(user_input)

        update_identity(user_input)

        print()

        print("AEVEX:", response)

        print()

