from fastapi import APIRouter

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("/", tags=["filtering"])
def filter_logs(query: str):
    return {"type": "LOG_SEARCH", "result": {"log 1": "1", "log 2": "1", "log 3": "1", "query was": query}}
