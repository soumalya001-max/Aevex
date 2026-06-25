from vector_memory.embedding_engine import generate_embedding
from vector_memory.vector_store import collection


def retrieve_context(
    query,
    top_k=5
):

    embedding = generate_embedding(
        query
    )

    results = collection.query(

        query_embeddings=[
            embedding
        ],

        n_results=top_k

    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    if not documents:

        return ""

    context = ""

    for doc in documents:

        context += doc
        context += "\n\n"

    return context