from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_rag

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: QuestionRequest):

    answer = ask_rag(
        request.question
    )

    return {
        "answer": answer
    }