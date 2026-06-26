import os
import subprocess
import psutil
import pyautogui
import time
import winapps
import pygetwindow as gw

from agents.verification_agent import VerificationAgent
from agents.retry_agent import RetryAgent


APP_EXECUTABLES = {

    "chrome": "chrome.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE",
    "spotify": "Spotify.exe",
    "discord": "Discord.exe",
    "calculator": "calc.exe",
    "settings": "ms-settings:",
    "explorer": "explorer.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "task manager": "taskmgr.exe"

}


STORE_APPS = {

    "xbox":
        "explorer shell:AppsFolder\\Microsoft.GamingApp_8wekyb3d8bbwe!App",

    "photos":
        "explorer shell:AppsFolder\\Microsoft.Windows.Photos_8wekyb3d8bbwe!App"

}


ALIASES = {

    "google chrome": "chrome",
    "browser": "chrome",

    "microsoft word": "word",
    "ms word": "word",

    "microsoft excel": "excel",

    "file explorer": "explorer",
    "windows explorer": "explorer",

    "calc": "calculator",

    "blue stacks": "bluestacks",

    "xbox app": "xbox"

}


PROTECTED_APPS = {
    "explorer.exe",
    "shellexperiencehost.exe",
    "startmenuexperiencehost.exe",
    "searchhost.exe",
    "dwm.exe"
}


def normalize_name(name):

    name = name.lower().strip()

    if name in ALIASES:
        return ALIASES[name]

    return name


def process_running(process_name):

    for proc in psutil.process_iter():

        try:

            if process_name.lower() in proc.name().lower():
                return True

        except:
            pass

    return False


def get_process_executable(app_name):
    app_name = normalize_name(app_name)
    executable = APP_EXECUTABLES.get(app_name)
    if executable:
        return executable
    return app_name.lower() + ".exe" if not app_name.lower().endswith(".exe") else app_name.lower()


def has_visible_window(process_name):
    try:
        all_windows = gw.getAllWindows()
        for window in all_windows:
            try:
                if window.visible and window.title and window.title.strip():
                    for proc in psutil.process_iter():
                        try:
                            proc_name = proc.name().lower()
                            if process_name.lower() in proc_name or proc_name in process_name.lower():
                                return True
                        except:
                            pass
            except:
                pass
    except:
        pass
    return False


def activate_existing_window(app_name):
    try:
        executable = get_process_executable(app_name)
        all_windows = gw.getAllWindows()
        for window in all_windows:
            try:
                if window.visible and window.title and window.title.strip():
                    for proc in psutil.process_iter():
                        try:
                            proc_name = proc.name().lower()
                            if executable.lower() in proc_name or app_name.lower() in proc_name:
                                try:
                                    window.activate()
                                    window.maximize()
                                    return True
                                except:
                                    pass
                        except:
                            pass
            except:
                pass
    except:
        pass
    return False


def launch_via_search(app_name):

    try:

        print(
            "[Launcher] Falling back to Windows Search..."
        )

        pyautogui.press("win")

        time.sleep(0.5)

        pyautogui.write(
            app_name,
            interval=0.03
        )

        time.sleep(0.5)

        pyautogui.press(
            "enter"
        )

        return True

    except:

        return False


def launch_native(app_name):

    try:

        executable = APP_EXECUTABLES.get(
            app_name
        )

        if executable is None:
            return False

        if executable.endswith(":"):

            os.system(
                f"start {executable}"
            )

        else:

            subprocess.Popen(
                executable,
                shell=True
            )

        return True

    except:
        return False


def launch_store_app(app_name):

    try:

        command = STORE_APPS.get(
            app_name
        )

        if command is None:
            return False

        subprocess.Popen(
            command,
            shell=True
        )

        return True

    except:
        return False


def launch_installed_program(app_name):

    try:

        for app in winapps.list_installed():

            if app_name in app.name.lower():

                subprocess.Popen(
                    app.install_location,
                    shell=True
                )

                return True

    except:
        pass

    return False


def open_application(app_name):

    app_name = normalize_name(
        app_name
    )

    executable = get_process_executable(app_name)

    if has_visible_window(executable):
        if activate_existing_window(app_name):
            return f"Activated existing {app_name} window"

    if process_running(app_name):
        return (
            f"{app_name} "
            f"is already running but has no visible window."
        )

    def execute_action():

        if launch_native(app_name):
            time.sleep(1)

            if VerificationAgent.verify_app_open(
                app_name
            ):
                return True

        if launch_installed_program(app_name):
            time.sleep(1)

            if VerificationAgent.verify_app_open(
                app_name
            ):
                return True

        if launch_store_app(app_name):
            time.sleep(1)

            if VerificationAgent.verify_app_open(
                app_name
            ):
                return True

        if launch_via_search(app_name):
            time.sleep(1)

            if VerificationAgent.verify_app_open(
                app_name
            ):
                return True

        return False

    result = RetryAgent.execute_with_retry(
        action="open",
        target=app_name,
        execute_function=execute_action,
        verify_function=lambda: VerificationAgent.verify_app_open(app_name),
        retries=3,
        delay=1
    )

    if result["success"]:
        return f"Successfully opened {app_name}"

    return result["message"]


def close_application(app_name):

    app_name = normalize_name(
        app_name
    )

    executable = get_process_executable(app_name)

    if executable in PROTECTED_APPS:
        closed_windows = close_visible_windows_for_app(app_name)
        if closed_windows:
            return f"Successfully closed {app_name} windows"
        return (
            f"{app_name} "
            f"has no visible windows."
        )

    if not process_running(app_name):

        return (
            f"{app_name} "
            f"is not running."
        )

    def execute_action():
        killed = False

        for proc in psutil.process_iter():

            try:

                if app_name in proc.name().lower():
                    proc.kill()
                    killed = True

            except:
                pass

        return killed

    result = RetryAgent.execute_with_retry(
        action="close",
        target=app_name,
        execute_function=execute_action,
        verify_function=lambda: VerificationAgent.verify_app_closed(app_name),
        retries=3,
        delay=1
    )

    if result["success"]:
        return f"Successfully closed {app_name}"

    return result["message"]


def close_visible_windows_for_app(app_name):
    try:
        executable = get_process_executable(app_name)
        all_windows = gw.getAllWindows()
        closed_any = False
        for window in all_windows:
            try:
                if window.visible and window.title and window.title.strip():
                    for proc in psutil.process_iter():
                        try:
                            proc_name = proc.name().lower()
                            if executable.lower() in proc_name or app_name.lower() in proc_name:
                                try:
                                    window.close()
                                    closed_any = True
                                except:
                                    pass
                        except:
                            pass
            except:
                pass
        return closed_any
    except:
        pass
    return False