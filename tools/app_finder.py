import os
import subprocess
import winreg


COMMON_PATHS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expandvars(
        r"%LOCALAPPDATA%\Programs"
    )
]


ALIASES = {

    "word": [
        "winword",
        "microsoft word",
        "ms word"
    ],

    "excel": [
        "microsoft excel",
        "spreadsheet"
    ],

    "chrome": [
        "google chrome",
        "browser"
    ],

    "explorer": [
        "file explorer",
        "files"
    ],

    "xbox": [
        "xbox app",
        "xbox game bar"
    ],

    "pw": [
        "physics wallah",
        "pw app"
    ],

    "discord": [
        "discord app"
    ],

    "spotify": [
        "spotify app"
    ]
}


def normalize(name):

    name = name.lower().strip()

    for canonical, aliases in ALIASES.items():

        if name == canonical:
            return canonical

        if name in aliases:
            return canonical

    return name


def open_via_start_menu(app_name):

    subprocess.Popen(
        [
            "powershell",
            "-Command",
            f'Start-Process "{app_name}"'
        ]
    )


def open_windows_search(app_name):

    subprocess.Popen(
        [
            "powershell",
            "-Command",
            f'Start-Process "shell:AppsFolder\\{app_name}"'
        ]
    )


def launch_app(app_name):

    app_name = normalize(app_name)

    try:

        open_via_start_menu(
            app_name
        )

        return True

    except Exception:

        pass

    try:

        open_windows_search(
            app_name
        )

        return True

    except Exception:

        return False