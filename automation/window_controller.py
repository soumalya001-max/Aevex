import pygetwindow as gw


def get_window():
    """Backward-compatible alias used by the rest of the app."""
    try:
        return gw.getActiveWindow()
    except Exception:
        return None


def _get_active_window():
    # internal helper
    return get_window()



def _find_visible_window_by_title(target_title: str):
    if not target_title:
        return None

    needle = str(target_title).strip().lower()
    if not needle:
        return None

    try:
        windows = gw.getWindowsWithTitle('')
    except Exception:
        windows = []

    # pygetwindow doesn't provide a direct "visible-only" filter consistently,
    # so we defensively check common attributes.
    for w in windows:
        try:
            title = getattr(w, "title", "") or ""
            if needle in str(title).lower():
                is_visible = getattr(w, "isVisible", True)
                if is_visible is False:
                    continue
                return w
        except Exception:
            continue

    return None


def maximize_window(target=None):
    try:
        if target is not None and str(target).strip() != "":
            window = _find_visible_window_by_title(target)
            if not window:
                return f"Window not found: {target}"
        else:
            window = _get_active_window()
            if not window:
                return "No active window."

        window.maximize()
        return "Window maximized."
    except Exception:
        # Never crash.
        if target is not None and str(target).strip() != "":
            return f"Window not found: {target}"
        return "No active window."


def minimize_window(target=None):
    try:
        if target is not None and str(target).strip() != "":
            window = _find_visible_window_by_title(target)
            if not window:
                return f"Window not found: {target}"
        else:
            window = _get_active_window()
            if not window:
                return "No active window."

        window.minimize()
        return "Window minimized."
    except Exception:
        if target is not None and str(target).strip() != "":
            return f"Window not found: {target}"
        return "No active window."


def restore_window(target=None):
    try:
        if target is not None and str(target).strip() != "":
            window = _find_visible_window_by_title(target)
            if not window:
                return f"Window not found: {target}"
        else:
            window = _get_active_window()
            if not window:
                return "No active window."

        window.restore()
        return "Window restored."
    except Exception:
        if target is not None and str(target).strip() != "":
            return f"Window not found: {target}"
        return "No active window."

