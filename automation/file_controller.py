import os
import shutil
from pathlib import Path
from send2trash import send2trash


DESKTOP = Path.home() / "Desktop"


def create_folder(name, location="desktop"):

    try:
        if location.lower() == "desktop":
            path = DESKTOP / name
        else:
            path = Path(location) / name

        path.mkdir(exist_ok=True)

        return f"Folder created: {path}"

    except Exception as e:
        return str(e)


def delete_item(name, location="desktop"):

    try:
        if location.lower() == "desktop":
            path = DESKTOP / name
        else:
            path = Path(location) / name

        if not path.exists():
            return "File or folder not found."

        send2trash(str(path))

        return f"Deleted {name}"

    except Exception as e:
        return str(e)


def rename_item(old_name, new_name, location="desktop"):

    try:
        if location.lower() == "desktop":
            old_path = DESKTOP / old_name
        else:
            old_path = Path(location) / old_name

        if not old_path.exists():
            return "File or folder not found."

        new_path = old_path.parent / new_name

        old_path.rename(new_path)

        return f"Renamed {old_name} to {new_name}"

    except Exception as e:
        return str(e)


def move_item(source, destination):

    try:
        shutil.move(source, destination)

        return "Move successful."

    except Exception as e:
        return str(e)


def copy_item(source, destination):

    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)

        return "Copy successful."

    except Exception as e:
        return str(e)