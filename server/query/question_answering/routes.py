import time

from fastapi import APIRouter
from server.query import log_qa
from server.query import generate_timestamp


# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
def qa(query: str, logId: str, top_n_lines: int = 1):
    top_n_lines = max(top_n_lines, 1)
    answer, ids = log_qa.generate_llm_answer(query, top_n_lines)
    logs = [{"lineId": i, "content": log_qa.get_log_line_by_id(i)} for i in ids]
    result = {
        "answer": answer,
        "timestamp": generate_timestamp(),
        "logs": logs,
    }
    return result
