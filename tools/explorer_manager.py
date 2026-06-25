import subprocess
import psutil


def explorer_running():

    for process in psutil.process_iter():

        try:

            if process.name().lower() == "explorer.exe":
                return True

        except Exception:
            pass

    return False


def open_explorer(new_window=False):

    if explorer_running() and not new_window:

        return (
            True,
            "File Explorer already open."
        )

    subprocess.Popen(
        "explorer"
    )

    return (
        True,
        "Opening File Explorer."
    )