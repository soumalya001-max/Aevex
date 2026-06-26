from functools import lru_cache


@lru_cache(maxsize=1)
def _load_embedding_model():

    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


def generate_embedding(text):

    model = _load_embedding_model()

    return model.encode(
        text

    ).tolist()