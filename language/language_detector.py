from langdetect import detect


def detect_language(text):

    text = text.lower()

    # Hinglish keywords

    hindi_words = [
        "hai",
        "kya",
        "kaise",
        "mera",
        "mujhe",
        "tum",
        "karna",
        "acha"
    ]

    # Banglish keywords

    bengali_words = [
        "ami",
        "amar",
        "kemon",
        "bhalo",
        "ache",
        "korchi",
        "chai"
    ]

    if any(word in text for word in bengali_words):

        return "bn"

    if any(word in text for word in hindi_words):

        return "hi"

    try:

        return detect(text)

    except:

        return "en"