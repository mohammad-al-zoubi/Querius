from fastapi import APIRouter
from server.helpers.utils import timestamp_to_custom_format
from server.query import log_qa_dict

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("", tags=["query"])
def summary(logId: str, prompt: str, lineFrom: int, lineTo: int, timeFrom: int, timeTo: int):
    timeFrom = timestamp_to_custom_format(timeFrom)
    timeTo = timestamp_to_custom_format(timeTo)
    log_qa = log_qa_dict.get(logId)
    result = log_qa.generate_dynamic_summary(prompt,
                                             start_id=lineFrom - 1,
                                             end_id=lineTo - 1,
                                             start_date=timeFrom,
                                             end_date=timeTo)
    return result
