import pyautogui


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


def search_google():

    pyautogui.hotkey(
        "ctrl",
        "l"
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

    return "Opened downloads."


def open_website(url):

    pyautogui.hotkey(
        "ctrl",
        "l"
    )

    pyautogui.typewrite(
        url
    )

    pyautogui.press(
        "enter"
    )

    return f"Opened website: {url}"
