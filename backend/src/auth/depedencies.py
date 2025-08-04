from fastapi import Request, status
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials
from src.auth.utils import decode_access_token

class AccessTokenBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        
        token = creds.credentials
        token_data = decode_access_token(token)

        if not self.token_valid(token):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or expired access token",
            )
        
        if token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access token cannot be a refresh token",
            )

        return creds
    
    def token_valid(self, token: str) -> bool:
        """Validate the access token."""

        try:
            token_data = decode_access_token(token)
            return token_data is not None
        except Exception:
            return False