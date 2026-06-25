import json

STATS_FILE = "data/provider_stats.json"


def load_stats():

    try:

        with open(
            STATS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return {}


def save_stats(stats):

    with open(
        STATS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            stats,
            file,
            indent=4
        )


def record_provider_success(provider):

    stats = load_stats()

    if provider not in stats:

        stats[provider] = {

            "successes": 0,

            "failures": 0

        }

    stats[provider]["successes"] += 1

    save_stats(stats)


def record_provider_failure(provider):

    stats = load_stats()

    if provider not in stats:

        stats[provider] = {

            "successes": 0,

            "failures": 0

        }

    stats[provider]["failures"] += 1

    save_stats(stats)


def show_statistics():

    stats = load_stats()

    return stats