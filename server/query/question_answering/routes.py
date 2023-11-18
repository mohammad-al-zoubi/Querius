import time

from fastapi import APIRouter

from server.logs.dummy import log_file_db
from server.query import log_qa
from server.helpers.utils import generate_timestamp


# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
def qa(query: str, logId: str, top_n_lines: int = 1):
    log_qa.set_session_parameters(log_file_db.get(logId))
    top_n_lines = max(top_n_lines, 1)
    answer, ids = log_qa.generate_llm_answer(query, top_n_lines)
    logs = []
    for i in ids:
        try:
            logs.append({"lineId": i, "content": log_qa.get_log_line_by_id(i)})
        except:
            pass
    result = {
        "answer": answer,
        "timestamp": generate_timestamp(),
        "logs": logs,
    }
    return result
