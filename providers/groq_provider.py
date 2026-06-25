from groq import Groq
from dotenv import load_dotenv

from models.groq_models import GROQ_MODELS

from core.provider_health import (
    can_use,
    record_success,
    record_failure
)

from core.model_ranker import (
    rank_models,
    record_success as rank_success,
    record_failure as rank_failure
)

import os

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def ask_groq(prompt: str):

    last_error = ""

    ranked_models = rank_models(
        GROQ_MODELS
    )

    for model in ranked_models:

        if not can_use(model):

            print(
                f"{model} cooling down..."
            )

            continue

        try:

            print(
                f"[Groq Model: {model}]"
            )

            response = client.chat.completions.create(

                model=model,

                messages=[

                    {
                        "role": "user",
                        "content": prompt
                    }

                ]

            )

            record_success(model)

            rank_success(model)

            return response.choices[0].message.content

        except Exception as e:

            record_failure(model)

            rank_failure(model)

            print(
                f"{model} failed"
            )

            print(
                str(e)
            )

            last_error = str(e)

    raise Exception(
        f"All Groq models failed.\n{last_error}"
    )