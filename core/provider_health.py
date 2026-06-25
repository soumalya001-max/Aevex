import json
import time

HEALTH_FILE = "data/model_health.json"


def load_health():

    try:

        with open(
            HEALTH_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return {}


def save_health(health):

    with open(
        HEALTH_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            health,
            file,
            indent=4
        )


def can_use(model):

    health = load_health()

    if model not in health:

        return True

    cooldown_until = health[model]["cooldown_until"]

    return time.time() > cooldown_until


def record_success(model):

    health = load_health()

    if model not in health:

        health[model] = {

            "successes": 0,
            "failures": 0,
            "cooldown_until": 0

        }

    health[model]["successes"] += 1

    save_health(health)


def record_failure(

        model,
        seconds=30

):

    health = load_health()

    if model not in health:

        health[model] = {

            "successes": 0,
            "failures": 0,
            "cooldown_until": 0

        }

    health[model]["failures"] += 1

    health[model]["cooldown_until"] = (

        time.time() + seconds

    )

    save_health(health)