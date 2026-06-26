import os
import math
import datetime
import shutil


# ----------------------------------
# CALCULATOR
# ----------------------------------

def calculate_expression(expression):

    try:

        allowed_names = {

            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round,
            "pi": math.pi,
            "e": math.e

        }

        result = eval(

            expression,

            {
                "__builtins__": None
            },

            allowed_names

        )

        return str(result)

    except Exception as e:

        return f"Calculation error: {e}"


# ----------------------------------
# CREATE FOLDER
# ----------------------------------

def create_folder(

    folder_name,
    location

):

    try:

        location = location.lower()

        if location == "desktop":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Desktop"

            )

        elif location == "documents":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Documents"

            )

        elif location == "downloads":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Downloads"

            )

        else:

            return (
                f"Unknown location: "
                f"{location}"
            )

        folder_path = os.path.join(

            base_path,
            folder_name

        )

        if os.path.exists(folder_path):

            return (
                f"Folder already exists: "
                f"{folder_name}"
            )

        os.makedirs(

            folder_path

        )

        return (
            f"Created folder "
            f"{folder_name} "
            f"in {location}"
        )

    except Exception as e:

        return (
            f"Folder creation failed: "
            f"{e}"
        )


# ----------------------------------
# CREATE FILE
# ----------------------------------

def create_file(

    filename,
    location="desktop"

):

    try:

        if location == "desktop":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Desktop"

            )

        elif location == "documents":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Documents"

            )

        else:

            return (
                f"Unknown location: "
                f"{location}"
            )

        file_path = os.path.join(

            base_path,
            filename

        )

        if os.path.exists(file_path):

            return (
                f"{filename} already exists."
            )

        with open(

            file_path,
            "w",
            encoding="utf-8"

        ) as f:

            f.write("")

        return (
            f"Created file "
            f"{filename}"
        )

    except Exception as e:

        return str(e)
    

# ----------------------------------
# CURRENT TIME
# ----------------------------------

def get_current_time():

    now = datetime.datetime.now()

    return now.strftime(

        "%I:%M %p"

    )


# ----------------------------------
# CURRENT DATE
# ----------------------------------

def get_current_date():

    today = datetime.date.today()

    return today.strftime(

        "%d-%m-%Y"

    )

# ----------------------------------
# DELETE FOLDER
# ----------------------------------

def delete_folder(

    folder_name,
    location

):

    try:

        location = location.lower()

        if location == "desktop":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Desktop"

            )

        elif location == "documents":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Documents"

            )

        elif location == "downloads":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Downloads"

            )

        else:

            return (
                f"Unknown location: "
                f"{location}"
            )

        folder_path = os.path.join(

            base_path,
            folder_name

        )

        

        if not os.path.exists(folder_path):

            return (
                f"Folder does not exist: "
                f"{folder_name}"
            )
        
        shutil.rmtree(

            folder_path

        )

        return (
            f"Deleted folder "
            f"{folder_name} "
            f"from {location}"
        )

    except Exception as e:

        return (
            f"Folder deletion failed: "
            f"{e}"
        )
    
# ----------------------------------
# RENAME FOLDER
# ----------------------------------

def rename_folder(

    folder_name,
    new_name,
    location

):

    try:

        location = location.lower()

        if location == "desktop":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Desktop"

            )

        elif location == "documents":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Documents"

            )

        elif location == "downloads":

            base_path = os.path.join(

                os.path.expanduser("~"),
                "Downloads"

            )

        else:

            return (
                f"Unknown location: "
                f"{location}"
            )

        folder_path = os.path.join(

            base_path,
            folder_name

        )

        new_folder_path = os.path.join(

            base_path,
            new_name

        )

        if not os.path.exists(folder_path):

            return (
                f"Folder does not exist: "
                f"{folder_name}"
            )

        if os.path.exists(new_folder_path):

            return (
                f"Folder already exists: "
                f"{new_name}"
            )

        os.rename(

            folder_path,
            new_folder_path

        )

        return (
            f"Renamed folder "
            f"{folder_name} "
            f"to {new_name} "
            f"in {location}"
        )

    except Exception as e:

        return (
            f"Folder rename failed: "
            f"{e}"
        )


# ----------------------------------
# COMMAND ENTRY POINT
# ----------------------------------

def execute_command(prompt):

    prompt = prompt.lower()

    # ----------------------
    # Time
    # ----------------------

    if "time" in prompt:

        return (
            f"Current time is "
            f"{get_current_time()}"
        )

    # ----------------------
    # Date
    # ----------------------

    if "date" in prompt:

        return (
            f"Today's date is "
            f"{get_current_date()}"
        )

    return None