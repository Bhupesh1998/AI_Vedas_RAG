import chromadb
from sentence_transformers import SentenceTransformer
from llm import generate_answer

# Load models once
model = SentenceTransformer("BAAI/bge-m3")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("garuda_purana")

DISTANCE_THRESHOLD = 1.2

def ask_rag(question):
    # Indented everything inside the function by 4 spaces
    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    best_distance = results["distances"][0][0]

    print("\nTOP DISTANCE:")
    print(best_distance)

    if best_distance > DISTANCE_THRESHOLD:
        return "या पुस्तकात याचे उत्तर सापडले नाही."

    context = "\n\n".join(results["documents"][0][:5])

    print("\n===== CONTEXT =====\n")
    print(context[:2000])
    print("\n===================\n")

    prompt = f"""
You are a retrieval-based book assistant.

RULES:

1. Use ONLY the provided CONTEXT.
2. Never use your own knowledge.
3. Never answer from training data.
4. Never guess.
5. Never infer.
6. Never summarize information that is not explicitly present in the context.
7. Every statement in the answer must be supported by the context.
8. If the answer is not explicitly found in the context, reply exactly:

या पुस्तकात याचे उत्तर सापडले नाही.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""


    return generate_answer(prompt)

if __name__ == "__main__":
    question = input("Question: ")
    answer = ask_rag(question)
    print("\n===== ANSWER =====\n")
    print(answer)
