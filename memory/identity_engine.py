import json

IDENTITY_FILE = "memory/identity.json"


def load_identity():

    try:

        with open(
            IDENTITY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return {}


def save_identity(identity):

    with open(
        IDENTITY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            identity,
            file,
            indent=4
        )


def update_identity(user_input):

    user_input = user_input.lower()

    identity = load_identity()

    # ---------------------------
    # PROJECTS
    # ---------------------------

    if "aevora" in user_input:
        identity["project"] = "Aevora"

    if "aevex" in user_input:
        identity["assistant_name"] = "Aevex"

    # ---------------------------
    # EDUCATION
    # ---------------------------

    if "jee" in user_input:
        identity["exam"] = "JEE"

    if "jee 2027" in user_input:
        identity["exam_year"] = "2027"

    # ---------------------------
    # FITNESS
    # ---------------------------

    if "muscle gain" in user_input:
        identity["fitness_goal"] = "Muscle Gain"

    if "fat loss" in user_input:
        identity["fitness_goal"] = "Fat Loss"

    # ---------------------------
    # CAREER
    # ---------------------------

    if "engineer" in user_input:
        identity["career_goal"] = "Engineer"

    save_identity(identity)


def build_identity_context():

    identity = load_identity()

    if not identity:
        return ""

    context = "Permanent Identity:\n\n"

    for key, value in identity.items():

        if value:

            context += f"{key}: {value}\n"

    return context