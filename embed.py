import json
import chromadb

from sentence_transformers import SentenceTransformer

print("Loading BGE Model...")

model = SentenceTransformer(
    "BAAI/bge-m3"
)

print("Loading Chunks...")

with open(
    "chunks.json",
    "r",
    encoding="utf-8"
) as file:

    chunks = json.load(file)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="garuda_purana"
)

print("Creating Embeddings...")

for i, chunk in enumerate(chunks):

    embedding = model.encode(
        chunk
    ).tolist()

    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[chunk]
    )

    if i % 20 == 0:
        print(f"Done {i}")

print("Finished!")