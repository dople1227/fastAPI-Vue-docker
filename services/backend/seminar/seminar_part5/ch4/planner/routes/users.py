from fastapi import APIRouter, HTTPException, status, Depends

from sqlmodel import select
from typing import List

from ..auth.jwt_handler import create_access_token
from ..auth.hash_password import HashPassword
from ..database.connection import get_session
from ..models.users import User, TokenResponse
from fastapi.security import OAuth2PasswordRequestForm

user_router = APIRouter(
    tags=["User"],
)
hash_password = HashPassword()


@user_router.get("", response_model=List[User])
async def retrieve_all_users(session=Depends(get_session)) -> List[User]:
    """모든 사용자 조회 라우팅함수"""
    statement = select(User)
    users = session.exec(statement).all()
    return users


@user_router.post("/signup")
async def sign_new_user(new_user: User, session=Depends(get_session)) -> dict:
    """사용자 등록"""

    # 등록된 사용자인지 체크
    select_user_exist = select(User).where(User.email == new_user.email)
    results = session.exec(select_user_exist)
    user_exist = results.first()

    # 이미 등록된 사용자면 HTTPException 발생
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="해당 이메일은 이미 등록된 사용자입니다.",
        )

    # 등록된 사용자가 아니면 INSERT
    hashed_password = hash_password.create_hash(new_user.password)
    new_user.password = hashed_password
    session.add(new_user)
    session.commit()
    # session.refresh(new_user)
    return {"message": "사용자가 등록되었습니다."}


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(
    user: OAuth2PasswordRequestForm = Depends(),
    session=Depends(get_session),
) -> dict:
    """사용자 로그인"""

    # DB에 존재하는 이메일 정보 가져옴
    select_user_exist = select(User).where(User.email == user.username)
    results = session.exec(select_user_exist)
    user_exist = results.first()

    # 존재 하지 않는다면 Exception
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="해당 이메일은 존재하지 않습니다."
        )

    # 패스워드가 일치하는지 인증정보 비교 후 인증에 성공하면 토큰 발행
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)

        return {"access_token": access_token, "token_type": "Bearer"}

    # 패스워드 불일치시 Exception 발생
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="패스워드가 일치하지 않거나 알 수 없는 오류가 발생했습니다.",
    )
