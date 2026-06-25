import os
import google.generativeai as genai

from dotenv import load_dotenv

from models.gemini_models import GEMINI_MODELS

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

load_dotenv()

genai.configure(

    api_key=os.getenv(
        "GEMINI_API_KEY"
    )

)


def ask_gemini(prompt: str):

    last_error = ""

    ranked_models = rank_models(
        GEMINI_MODELS
    )

    for model_name in ranked_models:

        if not can_use(model_name):

            print(
                f"{model_name} cooling down..."
            )

            continue

        try:

            print(
                f"[Gemini Model: {model_name}]"
            )

            model = genai.GenerativeModel(
                model_name
            )

            response = model.generate_content(
                prompt
            )

            record_success(model_name)

            rank_success(model_name)

            return response.text

        except Exception as e:

            record_failure(model_name)

            rank_failure(model_name)

            print(
                f"{model_name} failed"
            )

            print(
                str(e)
            )

            last_error = str(e)

    raise Exception(
        f"All Gemini models failed.\n{last_error}"
    )