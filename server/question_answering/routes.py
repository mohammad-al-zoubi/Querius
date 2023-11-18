from fastapi import APIRouter

# file in charge of summarization of logfiles

router = APIRouter()


@router.get("/", tags=["qa"])
def question_answering(question: str):
    return {"your question": question, "your answer": "abc"}
