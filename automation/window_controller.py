import pygetwindow as gw


def get_window():

    try:
        return gw.getActiveWindow()

    except:
        return None


def maximize_window():

    window = get_window()

    if not window:
        return "No active window."

    window.maximize()

    return "Window maximized."


def minimize_window():

    window = get_window()

    if not window:
        return "No active window."

    window.minimize()

    return "Window minimized."


def restore_window():

    window = get_window()

    if not window:
        return "No active window."

    window.restore()

    return "Window restored."