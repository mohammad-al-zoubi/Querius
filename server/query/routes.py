from fastapi import APIRouter, HTTPException
from starlette import status

from server.helpers.uuid_utils import is_valid_uuid
from server.query.log_search import routes as search
from server.query.summarization import routes as summarize
from server.query.question_answering import routes as qa
from server.query import log_qa
from server.logs.dummy import log_file_db

# Main router for querying
router = APIRouter()

router.include_router(summarize.router, prefix="/summary")
router.include_router(qa.router, prefix="/qa")
router.include_router(search.router, prefix="/search")


@router.post("/set_parameters", tags=["query"])
def set_session_parameters(file_path: str):
    log_qa.update_file_tracker()
    log_qa.set_session_parameters(file_path)
    return {"result": "parameters set successfully"}


@router.post("/get_logs_by_line_number", tags=["query"])
def get_logs_by_line_number(logId: str, line_number: int, neighbor_range: int = 0):
    if not is_valid_uuid(logId):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id provided is not valid",
        )
    log_qa.set_session_parameters(log_file_db.get(logId))
    line_number -= 1  # Compensate for offset
    neighbor_range = max(neighbor_range, 0)
    result = []
    for i in range(line_number - neighbor_range, line_number + neighbor_range + 1):
        try:
            result.append(log_qa.get_log_line_by_id(i))
        except:
            pass
    return result
