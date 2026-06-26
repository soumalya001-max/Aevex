import threading
import time

from core.router import ask_ai
from memory.memory_manager import add_conversation
from memory.semantic_memory import update_semantic_memory
from voice.speak import speak
from voice.wake_manager import WakeManager


def start_voice_mode():
    """Phase 5 voice mode: continuous background listening + wake word.

    Runs continuously until the user explicitly types `exit` in the terminal.
    """

    print("\nVOICE MODE STARTED (wake word: 'aevex' / 'hey aevex')\n")

    exit_event = threading.Event()
    wake_fired = threading.Event()

    def on_wake():
        # Callback runs from background thread.
        wake_fired.set()

    wm = WakeManager(on_wake=on_wake)
    wm.start()

    def _terminal_exit_watch():
        while not exit_event.is_set():
            try:
                cmd = input("")
                if cmd is not None and cmd.strip().lower() == "exit":
                    exit_event.set()
                    return
            except Exception:
                time.sleep(0.2)

    threading.Thread(target=_terminal_exit_watch, daemon=True).start()

    try:
        while not exit_event.is_set():
            # Passive wake polling.
            if not wake_fired.wait(timeout=0.2):
                continue

            wake_fired.clear()
            if exit_event.is_set():
                break

            # Minimal audible confirmation.
            try:
                speak("Yes?")
            except Exception:
                pass

            print("\n[Wake word detected] Recording command...")

            stop_for_command = threading.Event()
            cmd_text = wm.wait_for_command_text(stop_for_command)

            if exit_event.is_set():
                break

            if not cmd_text:
                print("AEVEX: (no speech detected)")
                continue

            if cmd_text.strip().lower() == "exit":
                speak("Goodbye")
                break

            print(f"You (voice): {cmd_text}")

            try:
                response = ask_ai(cmd_text)
            except Exception as e:
                response = "Sorry, I had trouble processing that."
                print("[Voice mode] ask_ai failed:", e)

            try:
                add_conversation(cmd_text, response)
                update_semantic_memory(cmd_text)
            except Exception:
                pass

            print("\nAEVEX:", response)

            try:
                speak(response)
            except Exception as e:
                print("[Voice mode] speak failed:", e)

    finally:
        try:
            wm.stop()
        except Exception:
            pass
        exit_event.set()

