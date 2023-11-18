from datetime import datetime, timedelta

from fastapi import APIRouter, Form, Depends, HTTPException
from starlette import status
from .db_helper import DBHelper
from .utils import *
# file in charge of summarization of logfiles
router = APIRouter()


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Check if account exists
    db_helper = DBHelper()
    if not db_helper.user_exists(username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. If you need an account, please contact your organization.",
        )
    # Check if provided password is correct
    pw_hash = db_helper.get_password_hash(username)
    if not compare_to_hash(password, pw_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. If you need an account, please contact your organization.",
        )
    # Return some tokens for auth
    organization = db_helper.get_organization(username)
    expiration_time = datetime.utcnow() + timedelta(minutes=15)
    payload = {
        "username": username,
        "organization": organization,
        "exp": expiration_time,
    }

    return create_token(payload)


@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    # Remove the token from the mock tokens database
    return {"message": "Logout successful"}
