PERMISSION_MODE = "user_approved"

# observer
# user_approved
# basic_auto
# full_auto


def ask_permission(action):

    global PERMISSION_MODE

    if PERMISSION_MODE == "observer":

        return False

    elif PERMISSION_MODE == "full_auto":

        return True

    elif PERMISSION_MODE == "basic_auto":

        return True

    else:

        answer = input(
            f"\nAllow action '{action}' ? (y/n): "
        )

        return answer.lower() == "y"