import psutil


def cpu_usage():

    return (
        f"CPU Usage: "
        f"{psutil.cpu_percent(interval=1)}%"
    )


def ram_usage():

    ram = psutil.virtual_memory()

    used = round(
        ram.used / 1024**3,
        2
    )

    total = round(
        ram.total / 1024**3,
        2
    )

    return (
        f"RAM Usage: "
        f"{ram.percent}% "
        f"({used}GB/{total}GB)"
    )