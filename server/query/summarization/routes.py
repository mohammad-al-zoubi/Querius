from fastapi import APIRouter

# file in charge of summarization of logfiles

router = APIRouter()


@router.get("/", tags=["summarize"])
def summarize(prompt: str):
    return {"your prompt": prompt, "your summary": "abc"}