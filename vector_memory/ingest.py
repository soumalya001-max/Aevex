import os
import chromadb

from sentence_transformers import SentenceTransformer
from vector_memory.chunker import chunk_text

from vector_memory.config import VECTOR_COLLECTION_NAME

collection = client.get_or_create_collection(
    name=VECTOR_COLLECTION_NAME
)

client = chromadb.PersistentClient(
    path="vector_memory/chroma_db"
)

collection = client.get_or_create_collection(
    name="aevex_knowledge"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def ingest_knowledge():

    knowledge_root = "knowledge"

    doc_id = 0

    for root, dirs, files in os.walk(knowledge_root):

        for filename in files:

            if not filename.endswith(".txt"):
                continue

            filepath = os.path.join(
                root,
                filename
            )

            try:

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as file:

                    text = file.read()

            except Exception as e:

                print(
                    f"Failed to read {filepath}: {e}"
                )

                continue

            chunks = chunk_text(text)

            for chunk in chunks:

                embedding = model.encode(
                    chunk
                ).tolist()

                collection.add(

                    ids=[
                        f"doc_{doc_id}"
                    ],

                    documents=[
                        chunk
                    ],

                    embeddings=[
                        embedding
                    ],

                    metadatas=[
                        {
                            "source": filepath
                        }
                    ]

                )

                doc_id += 1

    print(
        f"\nFinished ingesting {doc_id} chunks."
    )


if __name__ == "__main__":

    ingest_knowledge()