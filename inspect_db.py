import chromadb

client = chromadb.PersistentClient(
    path="vector_memory/chroma_db"
)

collection = client.get_collection(
    "aevex_knowledge"
)

data = collection.get()

print("\nDOCUMENTS:\n")

for doc in data["documents"]:
    print("=" * 50)
    print(doc)
    print()