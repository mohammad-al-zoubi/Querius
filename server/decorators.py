from fastapi import HTTPException
from starlette import status

from server.utils import context_is_set


def context_required(func):
    def wrapper(*args, **kwargs):
        if not context_is_set():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You need to set the context before using this feature",
            )
        return func(*args, **kwargs)

    return wrapper