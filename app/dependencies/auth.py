from fastapi import Header
from fastapi.exceptions import HTTPException
from typing import Optional
from services import check_key

async def require_api_key(x_api_key: Optional[str] = Header(None)):
    # If the header is missing or the key is invalid, raise a clean 401 Unauthorized error
    if not x_api_key or not check_key.verify(x_api_key):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API Key"
        )
