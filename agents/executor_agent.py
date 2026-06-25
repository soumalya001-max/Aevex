from automation.app_controller import open_application
from automation.app_controller import close_application

from automation.window_controller import (
    maximize_window,
    minimize_window,
    restore_window,
    get_window
)

from automation.browser_controller import (
    search_google,
    open_website,
    new_tab,
    close_tab,
    next_tab,
    previous_tab,
    scroll_down,
    scroll_up,
    refresh_page,
    go_back,
    go_forward,
    open_history,
    open_bookmarks,
    open_downloads
)

from commands.command_executor import (
    calculate_expression,
    create_folder,
    delete_folder,
    rename_folder
)


def execute_plan(plan):

    results = []

    for step in plan:

        action = step.get(
            "action"
        )

        # -------------------------
        # OPEN APP
        # -------------------------

        if action == "open_app":

            target = step.get(
                "target"
            )

            result = open_application(
                target
            )

            results.append(
                result
            )

        # -------------------------
        # CLOSE APP
        # -------------------------

        elif action == "close_app":

            target = step.get(
                "target"
            )

            result = close_application(
                target
            )

            results.append(
                result
            )

        # -------------------------
        # OPEN WEBSITE
        # -------------------------

        elif action == "open_website":

            url = step.get(
                "url"
            )

            result = open_website(
                url
            )

            results.append(
                result
            )

        # -------------------------
        # GOOGLE SEARCH
        # -------------------------

        elif action == "search_google":

            query = step.get(
                "query"
            )

            result = search_google(
                step["query"]
            )

            results.append(
                result
            )

        # -------------------------
        # CALCULATOR
        # -------------------------

        elif action == "calculate":

            expression = step.get(
                "expression"
            )

            result = calculate_expression(
                expression
            )

            results.append(
                str(result)
            )

        # -------------------------
        # CREATE FOLDER
        # -------------------------

        elif action == "create_folder":

            folder_name = step.get(
                "folder_name"
            )

            location = step.get(
                "location"
            )

            result = create_folder(
                folder_name,
                location
            )

            results.append(
                result
            )

        # -------------------------
        # DELETE FOLDER
        # -------------------------

        elif action == "delete_folder":

            folder_name = step.get(
                "folder_name"
            )

            location = step.get(
                "location"
            )

            result = delete_folder(
                folder_name,
                location
            )

            results.append(
                result
            )

         # -------------------------
        # RENAME FOLDER
        # -------------------------

        elif action == "rename_folder":

            folder_name = step.get(
                "folder_name"
            )

            location = step.get(
                "location"
            )

            result = rename_folder(
                folder_name,
                location
            )

            results.append(
                result
            )

        # -------------------------
        # MAXIMIZE WINDOW
        # -------------------------

        elif action == "maximize_window":

            window = step.get(
                "window"
            )

            result = maximize_window(
                window
            )

            results.append(
                result
            )

        # -------------------------
        # MINIMIZE WINDOW
        # -------------------------

        elif action == "minimize_window":

            window = step.get(
                "window"
            )

            result = minimize_window(
                window
            )

            results.append(
                result
            )

        # -------------------------
        # RESTORE WINDOW
        # -------------------------

        elif action == "restore_window":

            window = step.get(
                "window"
            )

            result = restore_window(
                window
            )

            results.append(
                result
            )

        # -------------------------
        # GET WINDOW
        # -------------------------

        elif action == "get_window":

            result = get_window()

            results.append(
                result
            )

        # -------------------------
        # NEW TAB
        # -------------------------

        elif action == "new_tab":

            result = new_tab()

            results.append(
                result
            )

        #-------------------------
        # CLOSE TAB
        #-------------------------

        elif action == "close_tab":

            result = close_tab()

            results.append(
                result
            )

        #-------------------------
        # NEXT TAB
        #-------------------------

        elif action == "next_tab":

            result = next_tab()

            results.append(
                result
            )

        #-------------------------
        # PREVIOUS TAB 
         #-------------------------
    
        elif action == "previous_tab":
    
            result = previous_tab()
    
            results.append(
                result
            )

        #-------------------------
        # SCROLL DOWN  
        #-------------------------

        elif action == "scroll_down":

            result = scroll_down()

            results.append(
                result
            )

        #-------------------------
        # SCROLL UP
        #-------------------------

        elif action == "scroll_up":

            result = scroll_up()

            results.append(
                result
            )

        #-------------------------
        # REFRESH PAGE 
        #-------------------------

        elif action == "refresh_page":

            result = refresh_page()

            results.append(
                result
            )

        #-------------------------
        # GO BACK
        #-------------------------

        elif action == "go_back":

            result = go_back()

            results.append(
                result
            )

        #-------------------------
        # GO FORWARD
        #-------------------------

        elif action == "go_forward":

            result = go_forward()

            results.append(
                result
            )

        #-------------------------
        # OPEN HISTORY
        #-------------------------

        elif action == "open_history":

            result = open_history()

            results.append(
                result
            )

        #-------------------------
        # OPEN BOOKMARKS
        #-------------------------

        elif action == "open_bookmarks":

            result = open_bookmarks()

            results.append(
                result
            )

        #-------------------------
        # OPEN DOWNLOADS
        #-------------------------

        elif action == "open_downloads":

            result = open_downloads()

            results.append(
                result
            )

    return results