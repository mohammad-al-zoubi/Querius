import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenHelper:
    def __init__(self):
        import os
        from dotenv import load_dotenv
        load_dotenv()
        self.SECRET_KEY = os.getenv("SECRET_KEY")

    def create_token(self, payload):
        return jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            # Handle expired token
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Something went wrong.",
            )

    def delete_token(self):
        # TODO
        # will delete token after logout
        pass

    def get_current_user(self, token: str = Depends(oauth2_scheme)):
        # Verify token and get user information
        decoded_data = self.decode_token(token)
        return decoded_data["username"]

