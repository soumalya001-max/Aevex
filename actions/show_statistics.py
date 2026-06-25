from core.statistics_manager import show_statistics


def execute_show_statistics():

    stats = show_statistics()

    if not stats:

        return "No statistics available."

    text = ""

    for provider in stats:

        text += (

            f"\n{provider}\n"

            f"Successes : {stats[provider]['successes']}\n"

            f"Failures : {stats[provider]['failures']}\n"

        )

    return text