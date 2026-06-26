def search_vector_memory(query, n_results=3):

    from vector_memory.embedding_engine import generate_embedding
    from vector_memory.vector_store import get_collection

    collection = get_collection()

    embedding = generate_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    return "\n\n".join(
        documents
    )