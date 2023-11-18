from fastapi import APIRouter

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
def summary(prompt: str):
    return {"type": "SUMMARY", "result": f"this is your summary to this prompt: {prompt}"}