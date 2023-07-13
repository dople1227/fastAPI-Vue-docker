import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from ..database.connection import Settings

settings = Settings()


def create_access_token(user: str):
    """토큰 생성 함수
    인증에 성공한 사용자에게 발행할 토큰을 생성.
    사용자명(이메일)과 만료일로 payload를 구성하고 시크릿키와 명시된 알고리즘으로
    토큰을 생성한다.
    """
    payload = {"user": user, "expires": time.time() + 3600}

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


def verify_access_token(token: str):
    """토큰 검증 함수
    사용자명(이메일)을 입력받아 시크릿키와 알고리즘으로 디코딩 후 만료일을 체크하여
    유효한 토큰인지 검증한다.
    """
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="액세스 토큰이 존재하지 않습니다.",
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="토큰이 만료되었습니다."
            )
        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="토큰정보가 잘못되었습니다."
        )
