import json
import time

MODEL_STATS_FILE = "data/model_stats.json"


def load_stats():

    try:

        with open(
            MODEL_STATS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return {}


def save_stats(stats):

    with open(
        MODEL_STATS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            stats,
            file,
            indent=4
        )


def initialize_model(model):

    stats = load_stats()

    if model not in stats:

        stats[model] = {

            "success": 0,
            "failure": 0,
            "score": 100,
            "last_success": 0,
            "last_failure": 0

        }

        save_stats(stats)


def record_success(model):

    stats = load_stats()

    initialize_model(model)

    stats = load_stats()

    stats[model]["success"] += 1
    stats[model]["score"] += 10
    stats[model]["last_success"] = time.time()

    save_stats(stats)


def record_failure(model):

    stats = load_stats()

    initialize_model(model)

    stats = load_stats()

    stats[model]["failure"] += 1
    stats[model]["score"] -= 25
    stats[model]["last_failure"] = time.time()

    if stats[model]["score"] < 0:

        stats[model]["score"] = 0

    save_stats(stats)


def rank_models(model_list):

    stats = load_stats()

    ranked = []

    for model in model_list:

        initialize_model(model)

        score = stats.get(
            model,
            {}
        ).get(
            "score",
            100
        )

        ranked.append(

            (
                model,
                score
            )

        )

    ranked.sort(

        key=lambda x: x[1],

        reverse=True

    )

    return [

        model[0]

        for model in ranked

    ]