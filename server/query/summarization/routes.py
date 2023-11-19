from fastapi import APIRouter

from server.decorators import context_required
from server.logs.dummy import log_file_db
from server.query import log_qa
from server.helpers.utils import timestamp_to_custom_format

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
@context_required
def summary(logId: str, prompt: str, lineFrom: int, lineTo: int, timeFrom: int, timeTo: int):
    timeFrom = timestamp_to_custom_format(timeFrom)
    timeTo = timestamp_to_custom_format(timeTo)
    print(prompt)
    print(lineFrom)
    print(lineTo)
    print(timeFrom)
    print(timeTo)
    result = log_qa.generate_dynamic_summary(prompt,
                                             start_id=lineFrom - 1,
                                             end_id=lineTo - 1,
                                             start_date=timeFrom,
                                             end_date=timeTo)
    return result
