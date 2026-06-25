import time
import psutil


def verify_process(process_names):

    time.sleep(2)

    running = []

    for process in psutil.process_iter():

        try:

            running.append(
                process.name().lower()
            )

        except Exception:
            pass

    for target in process_names:

        if target.lower() in running:
            return True

    return False