from rapidfuzz import process


KNOWN_ENTITIES = [

    "chrome",
    "youtube",
    "spotify",
    "discord",
    "facebook",
    "word",
    "excel",
    "powerpoint",
    "calculator",
    "notepad",
    "file explorer",
    "bluestacks",
    "xbox",
    "steam",
    "pw",
    "physics wallah"
]


def resolve_entity(name):

    result = process.extractOne(
        name,
        KNOWN_ENTITIES
    )

    if result is None:
        return name

    entity = result[0]
    score = result[1]

    if score > 70:
        return entity

    return name