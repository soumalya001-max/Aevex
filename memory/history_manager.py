import json

HISTORY_FILE = "memory/conversation_history.json"


def load_history():

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []


def build_recent_history(limit=10):

    history = load_history()

    recent_history = history[-limit:]

    formatted_history = ""

    for item in recent_history:

        user_message = item.get(
            "user",
            ""
        )

        assistant_message = item.get(
            "assistant",
            ""
        )

        formatted_history += (

            f"User: {user_message}\n"
            f"AEVEX: {assistant_message}\n\n"

        )

    return formatted_history