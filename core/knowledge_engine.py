import os


KNOWLEDGE_FOLDER = "knowledge"


def search_knowledge(query):

    query = query.lower()

    files = os.listdir(
        KNOWLEDGE_FOLDER
    )

    for file in files:

        if not file.endswith(".txt"):
            continue

        path = os.path.join(
            KNOWLEDGE_FOLDER,
            file
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        if query in content.lower():

            return content[:3000]

    return None