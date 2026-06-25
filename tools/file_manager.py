import os
import shutil


DESKTOP = os.path.join(
    os.path.expanduser("~"),
    "Desktop"
)


def create_folder(name):

    path = os.path.join(
        DESKTOP,
        name
    )

    try:

        os.makedirs(
            path,
            exist_ok=True
        )

        return (
            True,
            f"Folder {name} created."
        )

    except Exception as e:

        return (
            False,
            str(e)
        )


def delete_folder(name):

    path = os.path.join(
        DESKTOP,
        name
    )

    try:

        shutil.rmtree(path)

        return (
            True,
            f"Folder {name} deleted."
        )

    except Exception as e:

        return (
            False,
            str(e)
        )


def create_file(name):

    path = os.path.join(
        DESKTOP,
        name
    )

    try:

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:
            pass

        return (
            True,
            f"{name} created."
        )

    except Exception as e:

        return (
            False,
            str(e)
        )