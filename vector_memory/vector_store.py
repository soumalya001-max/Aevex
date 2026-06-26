from functools import lru_cache


@lru_cache(maxsize=1)
def _get_chroma_client():

    import chromadb

    return chromadb.PersistentClient(
        path="vector_memory/chroma_db"
    )


@lru_cache(maxsize=1)
def _get_collection():

    client = _get_chroma_client()

    return client.get_or_create_collection(
        name="aevex_knowledge"
    )


def get_client():

    return _get_chroma_client()


def get_collection():

    return _get_collection()


def reset_collection():

    import chromadb

    client = _get_chroma_client()

    try:

        client.delete_collection(
            "aevex_knowledge"
        )
    except:

        pass

    new_collection = client.get_or_create_collection(
        name="aevex_knowledge"
    )

    return new_collection