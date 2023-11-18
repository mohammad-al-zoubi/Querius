import time

from fastapi import APIRouter, HTTPException

from server.logs.dummy import log_file_db
from server.query import log_qa
from server.helpers.utils import generate_timestamp

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
def search(query: str, logId: str, top_n_lines: int = 1):
    try:
        log_qa.set_session_parameters(log_file_db.get(logId))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Something went terribly wrong! {type(e).__name__}")
    top_n_lines = max(top_n_lines, 1)
    try:
        logs = log_qa.log_search(query, top_n_lines)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Something went terribly wrong! {type(e).__name__}")
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
