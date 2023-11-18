from fastapi import APIRouter

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("/", tags=["qa"])
def question_answering(question: str):
    return {"type": "Q_AND_A", "result": f"your answer to this question '{question}'"}
