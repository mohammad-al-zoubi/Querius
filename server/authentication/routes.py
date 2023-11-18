from fastapi import APIRouter, Form, Depends
from .utils import *

# file in charge of summarization of logfiles

router = APIRouter()


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    #TODO
    # Return some tokens for auth
    return {"lorem": "ipsum"}


@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    # Remove the token from the mock tokens database

    return {"message": "Logout successful"}