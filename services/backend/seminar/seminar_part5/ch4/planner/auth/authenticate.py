from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    """토큰을 디코딩 하여 검증 후 인증에 사용되는 이메일 반환
    권한을 요구할 라우팅함수에 의존성을 주입하여 사용한다.
    의존성이 주입된 라우팅함수에 라우팅을 요청하려면
    Authorization헤더에 Bearer형식의 token을 함께 건내줘야함.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="해당 기능을 이용하려면 로그인이 필요합니다."
        )

    decoded_token = verify_access_token(token)
    return decoded_token["user"]
