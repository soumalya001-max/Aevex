import os


PERSONALITY_FOLDER = "personality"


def get_personality(task_type):

    mapping = {

        "general": "assistant.txt",

        "coding": "coder.txt",

        "reasoning": "researcher.txt",

        "study": "teacher.txt",

        "developer": "developer.txt"

    }

    filename = mapping.get(
        task_type,
        "assistant.txt"
    )

    path = os.path.join(
        PERSONALITY_FOLDER,
        filename
    )

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except:

        return ""