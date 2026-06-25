import psutil


PROCESS_ALIASES = {

    "chrome": [
        "chrome.exe"
    ],

    "word": [
        "winword.exe"
    ],

    "spotify": [
        "spotify.exe"
    ],

    "discord": [
        "discord.exe"
    ],

    "explorer": [
        "explorer.exe"
    ],

    "bluestacks": [
        "HD-Player.exe"
    ]
}


def is_running(app):

    app = app.lower()

    if app not in PROCESS_ALIASES:
        return False

    targets = PROCESS_ALIASES[app]

    for process in psutil.process_iter():

        try:

            if process.name() in targets:
                return True

        except Exception:
            pass

    return False


def kill_app(app):

    app = app.lower()

    if app not in PROCESS_ALIASES:
        return False

    targets = PROCESS_ALIASES[app]

    killed = False

    for process in psutil.process_iter():

        try:

            if process.name() in targets:

                process.kill()

                killed = True

        except Exception:
            pass

    return killed