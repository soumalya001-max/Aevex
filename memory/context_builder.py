from memory.memory_manager import load_memory
from memory.history_manager import build_recent_history
from memory.identity_engine import build_identity_context


def build_context():

    memory = load_memory()

    history = build_recent_history()

    identity_context = build_identity_context()

    context = ""

    # -------------------------
    # Identity
    # -------------------------

    context += identity_context

    # -------------------------
    # Semantic Memory
    # -------------------------

    if memory:

        context += "\nKnown Information:\n\n"

        for key, value in memory.items():

            context += f"{key}: {value}\n"

    # -------------------------
    # Conversation History
    # -------------------------

    context += "\nRecent Conversations:\n\n"

    context += history

    return context