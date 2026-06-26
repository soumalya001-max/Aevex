import os
import time
import psutil
import pygetwindow as gw


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


WEBSITE_KEYWORDS = {
    "youtube": ["youtube", "youtube.com", "yt"],
    "gmail": ["gmail", "mail.google", "google mail"],
    "github": ["github", "github.com"],
    "chatgpt": ["chatgpt", "chat.openai", "openai"],
    "facebook": ["facebook", "facebook.com", "fb"],
    "instagram": ["instagram", "instagram.com", "ig"],
    "discord": ["discord", "discord.com"],
    "pw": ["pw.live", "pw", "physics wallah"]
}


def normalize_name(name):

    name = name.lower().strip()

    if name in ALIASES:
        return ALIASES[name]

    return name


def get_process_executable(app_name):
    app_name = normalize_name(app_name)
    executable = APP_EXECUTABLES.get(app_name)
    if executable:
        return executable
    return app_name.lower() + ".exe" if not app_name.lower().endswith(".exe") else app_name.lower()


def has_visible_window(executable_name):
    try:
        all_windows = gw.getAllWindows()
        for window in all_windows:
            try:
                if window.visible and window.title and window.title.strip():
                    return True
            except:
                pass
    except:
        pass
    return False


class VerificationAgent:

    @staticmethod
    def get_process_names(app_name):

        app_name = normalize_name(
            app_name
        )

        names_to_check = set()

        names_to_check.add(
            app_name.lower()
        )

        executable = APP_EXECUTABLES.get(
            app_name
        )

        if executable:
            names_to_check.add(
                executable.lower()
            )

            executable_without_ext = (
                executable.lower()
                .replace(".exe", "")
            )

            names_to_check.add(
                executable_without_ext
            )

        return names_to_check

    @staticmethod
    def verify_app_open(
        app_name,
        timeout=5
    ):

        process_names = (
            VerificationAgent
            .get_process_names(
                app_name
            )
        )

        start_time = time.time()

        while (
            time.time() - start_time
            < timeout
        ):

            try:
                all_windows = gw.getAllWindows()
                for window in all_windows:
                    try:
                        if window.visible and window.title and window.title.strip():
                            for proc in psutil.process_iter():
                                try:
                                    proc_name = proc.name().lower()
                                    for target in process_names:
                                        if target in proc_name:
                                            return True
                                except:
                                    pass
                    except:
                        pass
            except:
                pass

            time.sleep(0.5)

        return False

    @staticmethod
    def verify_app_closed(
        app_name,
        timeout=5
    ):

        process_names = (
            VerificationAgent
            .get_process_names(
                app_name
            )
        )

        start_time = time.time()

        while (
            time.time() - start_time
            < timeout
        ):

            found_process = False
            found_visible = False

            for proc in psutil.process_iter():

                try:
                    process_name = (
                        proc.name()
                        .lower()
                    )

                    for target in process_names:

                        if (
                            target
                            in process_name
                        ):

                            found_process = True
                            break

                    if found_process:
                        break

                except:
                    pass

            if found_process:
                try:
                    all_windows = gw.getAllWindows()
                    for window in all_windows:
                        try:
                            if window.visible and window.title and window.title.strip():
                                found_visible = True
                                break
                        except:
                            pass
                except:
                    pass

                if not found_visible:
                    return True

            time.sleep(
                0.5
            )

        return False

    @staticmethod
    def verify_window_exists(
        title,
        timeout=5
    ):

        start_time = time.time()

        while (
            time.time() - start_time
            < timeout
        ):

            try:
                windows = (
                    gw.getAllTitles()
                )

                for window in windows:

                    if (
                        title.lower()
                        in window.lower()
                    ):

                        return True

            except:
                pass

            time.sleep(
                0.5
            )

        return False

    @staticmethod
    def verify_file_exists(
        path
    ):

        return os.path.exists(
            path
        )

    @staticmethod
    def verify_folder_exists(
        path
    ):

        return os.path.isdir(
            path
        )

    @staticmethod
    def verify_website_open(
        website_name,
        timeout=8
    ):

        website_name = website_name.lower().strip()

        keywords = None
        for key, words in WEBSITE_KEYWORDS.items():
            if website_name == key or website_name in words:
                keywords = words
                break

        if not keywords:
            if " " in website_name:
                keywords = [website_name.replace(" ", "")]
            else:
                keywords = [website_name]

        start_time = time.time()

        while (
            time.time() - start_time
            < timeout
        ):
            try:
                chrome_found = False
                for proc in psutil.process_iter():
                    try:
                        if "chrome" in proc.name().lower():
                            chrome_found = True
                            break
                    except:
                        pass

                if not chrome_found:
                    return False

                windows = gw.getAllTitles()
                for window in windows:
                    try:
                        window_lower = window.lower()
                        for keyword in keywords:
                            if keyword in window_lower:
                                for excl in ["uninstall", "setup", "installer"]:
                                    if excl in window_lower:
                                        continue
                                return True
                    except:
                        pass

            except Exception:
                pass

            time.sleep(0.5)

        return False