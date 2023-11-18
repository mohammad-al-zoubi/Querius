from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Verify token and get user information
    # TODO
    # check if token is valid, if is then return infos of user
    if True:
        return "RS"
    else:
        raise HTTPException(status_code=401, detail="Invalid token")


def create_token():
    # TODO
    # create some tokens for auth
    return "very useful token"


def delete_token():
    # TODO
    # will delete token after logout
    pass
