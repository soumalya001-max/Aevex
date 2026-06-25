import webbrowser
import urllib.parse


WEBSITES = {

    "youtube":
        "https://youtube.com",

    "facebook":
        "https://facebook.com",

    "discord":
        "https://discord.com/app",

    "spotify":
        "https://open.spotify.com",

    "pw":
        "https://www.pw.live",

    "physics wallah":
        "https://www.pw.live",

    "gmail":
        "https://mail.google.com",

    "chatgpt":
        "https://chatgpt.com",

    "github":
        "https://github.com"
}


def open_website(name):

    key = name.lower()

    if key not in WEBSITES:

        return (
            False,
            "Unknown website."
        )

    webbrowser.open(
        WEBSITES[key]
    )

    return (
        True,
        f"Opening {name}."
    )


def google_search(query):

    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return (
        True,
        f"Searching for {query}"
    )


def youtube_search(query):

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return (
        True,
        f"Searching YouTube for {query}"
    )