from openai import OpenAI
from dotenv import load_dotenv
from models.openrouter_models import OPENROUTER_MODELS

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

client = OpenAI(

    api_key=os.getenv(
        "OPENROUTER_API_KEY"
    ),

    base_url="https://openrouter.ai/api/v1"

)


def ask_openrouter(prompt):

    last_error = ""

    ranked_models = rank_models(
        OPENROUTER_MODELS
    )

    for model in ranked_models:

        if not can_use(model):

            print(
                f"{model} cooling down..."
            )

            continue

        try:

            print(
                f"[OpenRouter Model: {model}]"
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

            last_error = str(e)

    raise Exception(last_error)