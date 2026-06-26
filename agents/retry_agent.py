import time
import psutil
import pygetwindow as gw

from agents.escalation_agent import EscalationAgent


CLOSED_BY_USER_STATE = {}


class RetryAgent:

    @staticmethod
    def execute_with_retry(
        action,
        target,
        execute_function,
        verify_function,
        retries=3,
        delay=1
    ):
        last_error = None
        user_closed_key = f"{action}_{target}"
        CLOSED_BY_USER_STATE[user_closed_key] = False

        for attempt in range(retries):
            try:
                if attempt > 0:
                    print(
                        f"[Retry] Sequence retry {attempt + 1}/"
                        f"{retries} for '{action}' on '{target}'"
                    )

                result = execute_function()

                if result:
                    if verify_function():
                        CLOSED_BY_USER_STATE[user_closed_key] = False
                        return {
                            "success": True,
                            "message": f"Successfully {action}ed {target}"
                        }
                    else:
                        print(
                            f"[Verify] Verification failed for '{target}', "
                            f"moving to next fallback method"
                        )

                        if action == "open" and RetryAgent._detect_user_closed_during_open(target):
                            CLOSED_BY_USER_STATE[user_closed_key] = True
                            return {
                                "success": False,
                                "message": f"Application was opened but closed by user."
                            }

                else:
                    print(
                        f"[Launcher] All launch methods failed for '{target}' "
                        f"in this sequence attempt"
                    )

            except Exception as e:
                last_error = str(e)
                print(
                    f"[Error] {e}"
                )

            if attempt < retries - 1:
                time.sleep(delay)

        if CLOSED_BY_USER_STATE.get(user_closed_key, False):
            return {
                "success": False,
                "message": f"Application was opened but closed by user."
            }

        return {
            "success": False,
            "message": EscalationAgent.escalate(
                action,
                target
            )
        }

    @staticmethod
    def _detect_user_closed_during_open(app_name):
        try:
            all_windows = gw.getAllWindows()
            for window in all_windows:
                try:
                    if window.visible and window.title and window.title.strip():
                        return False
                except:
                    pass
            return True
        except:
            return False