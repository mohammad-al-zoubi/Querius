import time

from fastapi import APIRouter
from server.query import log_qa
from server.query import generate_timestamp

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
def search(query: str, logId: str, top_n_lines: int = 1):
    top_n_lines = max(top_n_lines, 1)
    logs = log_qa.log_search(query, top_n_lines)
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
