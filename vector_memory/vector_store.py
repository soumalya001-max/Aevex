import chromadb

client = chromadb.PersistentClient(
    path="vector_memory/chroma_db"
)

collection = client.get_or_create_collection(
    name="aevex_knowledge"
)


def reset_collection():

    global collection

    try:

        client.delete_collection(
            "aevex_knowledge"
        )
    except:
        pass

    collection = client.get_or_create_collection(
        name="aevex_knowledge"
    )