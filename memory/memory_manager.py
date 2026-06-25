import json

MEMORY_FILE = "memory/memory.json"
HISTORY_FILE = "memory/conversation_history.json"


# ---------- MEMORY ----------

def load_memory():

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    except:

        return {}


def save_memory(memory):

    print("Writing to:", MEMORY_FILE)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            memory,
            file,
            indent=4
        )

    print("Memory write completed.")


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):

    memory = load_memory()

    return memory.get(key)


def show_memory():

    return load_memory()


# ---------- CONVERSATION HISTORY ----------

def load_history():

    try:

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    except:

        return []


def save_history(history):

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            history,
            file,
            indent=4
        )


def add_conversation(user_message, assistant_reply):

    history = load_history()

    history.append(

        {
            "user": user_message,
            "assistant": assistant_reply
        }

    )

    history = history[-20:]

    save_history(history)