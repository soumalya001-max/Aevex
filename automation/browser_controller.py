import pyautogui
import time

from agents.verification_agent import VerificationAgent
from agents.retry_agent import RetryAgent


WEBSITE_MAP = {

    "youtube":
        "https://www.youtube.com",

    "gmail":
        "https://mail.google.com",

    "facebook":
        "https://www.facebook.com",

    "instagram":
        "https://www.instagram.com",

    "github":
        "https://github.com",

    "chatgpt":
        "https://chatgpt.com",

    "discord":
        "https://discord.com/app",

    "pw":
        "https://www.pw.live"

}


def new_tab():

    pyautogui.hotkey(
        "ctrl",
        "t"
    )

    return "Opened new tab."


def close_tab():

    pyautogui.hotkey(
        "ctrl",
        "w"
    )

    return "Closed current tab."


def next_tab():

    pyautogui.hotkey(
        "ctrl",
        "tab"
    )

    return "Moved to next tab."


def previous_tab():

    pyautogui.hotkey(
        "ctrl",
        "shift",
        "tab"
    )

    return "Moved to previous tab."


def search_google(query=None):

    pyautogui.hotkey(
        "ctrl",
        "l"
    )

    if query:
        pyautogui.write(
            query,
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        return (
            f"Searched Google for "
            f"{query}"
        )

    return "Focused on the search bar."


def scroll_down():

    pyautogui.scroll(
        -500
    )

    return "Scrolled down."


def scroll_up():

    pyautogui.scroll(
        500
    )

    return "Scrolled up."


def refresh_page():

    pyautogui.hotkey(
        "ctrl",
        "r"
    )

    return "Refreshed the page."


def go_back():

    pyautogui.hotkey(
        "alt",
        "left"
    )

    return "Went back to the previous page."


def go_forward():

    pyautogui.hotkey(
        "alt",
        "right"
    )

    return "Went forward to the next page."


def open_history():

    pyautogui.hotkey(
        "ctrl",
        "h"
    )

    return "Opened browsing history."


def open_bookmarks():

    pyautogui.hotkey(
        "ctrl",
        "shift",
        "b"
    )

    return "Opened bookmarks."


def open_downloads():

    pyautogui.hotkey(
        "ctrl",
        "j"
    )

    return "Opened download."


def open_website(url):

    original_url = url
    url = url.lower().strip()

    if url in WEBSITE_MAP:
        url = WEBSITE_MAP[url]

    elif not url.startswith(
        "http"
    ):

        url = (
            "https://"
            + url
        )

    def execute_action():
        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(
            0.2
        )

        pyautogui.write(
            url,
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        return True

    result = RetryAgent.execute_with_retry(
        action="open",
        target=original_url,
        execute_function=execute_action,
        verify_function=lambda: VerificationAgent.verify_website_open(original_url),
        retries=3,
        delay=1
    )

    if result["success"]:
        return f"Successfully opened website: {url}"

    return result["message"]