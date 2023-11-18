from fastapi import Depends, HTTPException
from starlette import status
from authentication import oauth2_scheme
from helpers import token_helper


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = token_helper.decode_token(token)
    username: str = payload.get("username")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return username


def get_current_organization(token: str = Depends(oauth2_scheme)):
    payload = token_helper.decode_token(token)
    organization: str = payload.get("organization")
    if organization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return organization
