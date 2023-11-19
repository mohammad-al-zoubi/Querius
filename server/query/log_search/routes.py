import time

from fastapi import APIRouter, HTTPException
from starlette import status

from server.decorators import context_required
from server.logs.dummy import log_file_db
from server.query import log_qa
from server.helpers.utils import generate_timestamp

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
@context_required
def search(query: str, logId: str, top_n_lines: int = 1):
    top_n_lines = max(top_n_lines, 1)
    try:
        logs = log_qa.log_search(query, top_n_lines)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Something went terribly wrong!")
    logs_formated = []
    for log in logs:
        temp = {
            "lineId": log.get("id"),
            "content": log.get("logline")
        }
        logs_formated.append(temp)
    result = {
        "timestamp": generate_timestamp(),
        "logId": logId,
        "LogLine": logs_formated
    }
    return result
