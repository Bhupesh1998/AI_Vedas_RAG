import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-m3"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "garuda_purana"
)

query = input("Question: ")

query_embedding = model.encode(
    query
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

context = "\n\n".join(
    results["documents"][0]
)

print(context)

# print("\nTOP RESULTS:\n")

# for doc in results["documents"][0]:

#     print("=" * 50)
#     print(doc[:1000])