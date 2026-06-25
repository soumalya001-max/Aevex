import psutil


def cpu_usage():

    return f"CPU Usage: {psutil.cpu_percent()}%"


def ram_usage():

    return (
        f"RAM Usage: "
        f"{psutil.virtual_memory().percent}%"
    )


def running_processes():

    processes = []

    for p in psutil.process_iter():

        try:

            processes.append(
                p.name()
            )

        except:
            pass

    return processes