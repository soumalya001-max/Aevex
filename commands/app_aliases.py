APP_ALIASES = {

    # Browsers
    "chrome": "chrome",
    "google chrome": "chrome",

    "edge": "msedge",
    "microsoft edge": "msedge",

    "firefox": "firefox",

    "brave": "brave",

    "opera": "opera",

    # Office
    "word": "winword",
    "microsoft word": "winword",
    "ms word": "winword",

    "excel": "excel",
    "microsoft excel": "excel",

    "powerpoint": "powerpnt",
    "power point": "powerpnt",
    "microsoft powerpoint": "powerpnt",

    # Windows Apps
    "calculator": "calc",
    "calc": "calc",

    "notepad": "notepad",

    "paint": "mspaint",

    "settings": "ms-settings:",
    "windows settings": "ms-settings:",

    "task manager": "taskmgr",

    "file explorer": "explorer",
    "explorer": "explorer",

    "command prompt": "cmd",
    "cmd": "cmd",

    "powershell": "powershell",

    # Development
    "vscode": "code",
    "vs code": "code",
    "visual studio code": "code",

    "pycharm": "pycharm64",

    "android studio": "studio64",

    # Entertainment
    "spotify": "spotify",

    "steam": "steam",

    "discord": "discord",

    "telegram": "telegram",

    "whatsapp": "whatsapp",

    "bluestacks": "HD-Player",
    "blue stacks": "HD-Player",

    # Gaming
    "xbox": "xbox",

    "epic games": "epicgameslauncher",

    "epic games launcher": "epicgameslauncher",

    "riot client": "riotclientservices",

    # Utilities
    "camera": "windowscamera",

    "snipping tool": "snippingtool",

    "photos": "photos"
}


def resolve_alias(app_name):

    app_name = app_name.lower().strip()

    return APP_ALIASES.get(
        app_name,
        app_name
    )