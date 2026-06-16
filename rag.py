import chromadb
from sentence_transformers import SentenceTransformer
from ollama import chat

model = SentenceTransformer(
    "BAAI/bge-m3"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "garuda_purana"
)

question = input("Question: ")

query_embedding = model.encode(
    question
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

best_distance = results["distances"][0][0]

print("\nTOP DISTANCE:")
print(best_distance)

if best_distance > 1.2:
    print("\nया पुस्तकात याचे उत्तर सापडले नाही.")
    exit()

context = "\n\n".join(
    # results["documents"][0]
    results["documents"][0][:3]
)


print("\n===== CONTEXT =====\n")
print(context[:3000])
print("\n===================\n")

prompt = f"""
You are a book assistant.

Rules:

1. Answer ONLY from the provided context.
2. Do NOT add your own knowledge.
3. Do NOT infer or assume anything.
4. Quote relevant lines from context when possible.
5. If answer is not found, say:
   "या पुस्तकात याचे उत्तर सापडले नाही."

CONTEXT:
{context}

QUESTION:
{question}
"""

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "system",
            "content": """
You are a retrieval-based book assistant.

Rules:

1. Use ONLY the provided context.
2. Never use your own knowledge.
3. Never answer from training data.
4. If the answer is not explicitly found in the context, reply exactly:

या पुस्तकात याचे उत्तर सापडले नाही.

5. Do not guess.
6. Do not infer.
"""
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n")
print(response["message"]["content"])