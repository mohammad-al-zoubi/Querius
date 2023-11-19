from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from server.helpers.auth_utils import get_current_organization
from .db_helper import DBHelper
from server.helpers.uuid_utils import is_valid_uuid
from .dummy import log_file_db

router = APIRouter()


@router.get("/all", tags=["logs"])
def get_all_logs(organization: str = Depends(get_current_organization)):
    db_helper = DBHelper()
    return db_helper.get_log_list(organization)


@router.get("/{log_uuid}", tags=["logs"])
def get_log(log_uuid: str, organization: str = Depends(get_current_organization)):
    if not is_valid_uuid(log_uuid):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The id provided is not valid",
        )
    db_helper = DBHelper()
    log = db_helper.get_log(organization, log_uuid)
    return log
