from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/chat")
def chat(question_data: Question):

    question = question_data.question

    # ata temporary
    answer = f"Question hota: {question}"

    return {
        "answer": answer
    }