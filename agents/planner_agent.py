import re


def create_plan(prompt):

    prompt_lower = prompt.lower()

    plan = []

    # --------------------------------------------------
    # OPEN APPLICATION
    # --------------------------------------------------

    open_match = re.search(
        r"open (.+)",
        prompt_lower
    )

    if open_match:

        target = open_match.group(1)

        # Strip window/launch modifiers from target
        modifiers = [
            "in a new window", "in new window", "new window of",
            "in chrome", "in firefox", "in edge", "in browser",
            "in a new tab", "in new tab", "new tab",
            "in background", "in the background",
            "as administrator", "as admin",
        ]
        for mod in modifiers:
            target = target.replace(mod, "").strip()

        if (
            "youtube" in target or
            "facebook" in target or
            "instagram" in target or
            "gmail" in target or
            "discord" in target or
            "pw" in target or
            "github" in target or
            "chatgpt" in target
        ):

            plan.append({

                "action": "open_website",

                "url": target.strip()

            })

        else:

            plan.append({

                "action": "open_app",

                "target": target.strip()

            })

    # --------------------------------------------------
    # CLOSE APPLICATION
    # --------------------------------------------------

    close_match = re.search(
        r"close (.+)",
        prompt_lower
    )

    if close_match:

        target = close_match.group(1)

        # Strip window/launch modifiers from target
        modifiers = [
            "in a new window", "in new window", "new window of",
            "in chrome", "in firefox", "in edge", "in browser",
            "in a new tab", "in new tab", "new tab",
            "in background", "in the background",
            "as administrator", "as admin",
        ]
        for mod in modifiers:
            target = target.replace(mod, "").strip()

        if "tab" in target:

            plan.append({

                "action": "close_tab"

            })

        else:

            plan.append({

                "action": "close_app",

                "target": target.strip()

            })

    # --------------------------------------------------
    # GOOGLE SEARCH
    # --------------------------------------------------

    search_match = re.search(
        r"search (.+)",
        prompt_lower
    )

    if search_match:

        query = search_match.group(1)

        query = query.replace(
            "in chrome",
            ""
        ).strip()

        plan.append({

            "action": "search_google",

            "query": query

        })

    # --------------------------------------------------
    # CALCULATOR
    # --------------------------------------------------

    expression_match = re.search(
        r"calculate (.+)",
        prompt_lower
    )

    if expression_match:

        expression = expression_match.group(1)

        plan.append({

            "action": "calculate",

            "expression": expression

        })

    # --------------------------------------------------
    # CREATE FOLDER
    # --------------------------------------------------

    folder_match = re.search(
        r"create a folder named (.+?) in (.+)",
        prompt_lower
    )

    if folder_match:

        folder_name = folder_match.group(1)

        location = folder_match.group(2)

        plan.append({

            "action": "create_folder",

            "folder_name": folder_name.strip(),

            "location": location.strip()

        })

    # --------------------------------------------------
    # DELETE FOLDER
    # --------------------------------------------------

    delete_match = re.search(
        r"(delete|remove) folder (.+)",
        prompt_lower
    )

    if delete_match:

        folder_name = delete_match.group(2)

        plan.append({

            "action": "delete_folder",

            "folder_name": folder_name.strip()

        })

    # --------------------------------------------------
    # RENAME FOLDER
    # --------------------------------------------------

    rename_match = re.search(
        r"rename folder (.+?) to (.+)",
        prompt_lower
    )

    if rename_match:

        old_name = rename_match.group(1)

        new_name = rename_match.group(2)

        plan.append({

            "action": "rename_folder",

            "old_name": old_name.strip(),

            "new_name": new_name.strip()

        })

    # --------------------------------------------------
    # WINDOW MANAGEMENT
    # --------------------------------------------------

    if "maximize" in prompt_lower:

        target = prompt_lower.replace(
            "maximize",
            ""
        ).strip()

        plan.append({

            "action": "maximize_window",

            "target": target

        })

    if "minimize" in prompt_lower:

        target = prompt_lower.replace(
            "minimize",
            ""
        ).strip()

        plan.append({

            "action": "minimize_window",

            "target": target

        })

    if "restore" in prompt_lower:

        target = prompt_lower.replace(
            "restore",
            ""
        ).strip()

        plan.append({

            "action": "restore_window",

            "target": target

        })

    # --------------------------------------------------
    # TAB CONTROL
    # --------------------------------------------------

    if "open new tab" in prompt_lower:

        plan.append({

            "action": "open_tab"

        })

    if "next tab" in prompt_lower:

        plan.append({

            "action": "next_tab"

        })

    if "previous tab" in prompt_lower:

        plan.append({

            "action": "previous_tab"

        })

    # --------------------------------------------------
    # SYSTEM MONITORING
    # --------------------------------------------------

    if "cpu usage" in prompt_lower:

        plan.append({

            "action": "cpu_usage"

        })

    if (
        "ram usage" in prompt_lower or
        "memory usage" in prompt_lower
    ):

        plan.append({

            "action": "ram_usage"

        })

    return plan