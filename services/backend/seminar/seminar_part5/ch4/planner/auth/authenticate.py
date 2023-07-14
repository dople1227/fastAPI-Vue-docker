from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    """토큰을 검증하여 인증에 사용되는 이메일 반환
    검증이 필요한 라우팅함수에 의존성 추가하여 사용.
    이 함수가 의존성 주입된 라우팅 함수에 라우팅을 요청하려면
    Authorization헤더에 Bearer형식의 token을 함께 건내줘야함.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="해당 기능을 이용하려면 로그인이 필요합니다."
        )

    decoded_token = verify_access_token(token)
    return decoded_token["user"]
