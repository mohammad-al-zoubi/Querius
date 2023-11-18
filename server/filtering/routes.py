from fastapi import APIRouter

# file in charge of summarization of logfiles

router = APIRouter()


@router.get("/", tags=["filtering"])
def filter_logs(query: str):
    return {"your query": query, "your result": "abc"}
