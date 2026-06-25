import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="vector_memory/chroma_db"
)

collection = client.get_collection(
    name="aevex_knowledge"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def search_vector_memory(query, n_results=3):

    embedding = model.encode(
        query
    ).tolist()

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