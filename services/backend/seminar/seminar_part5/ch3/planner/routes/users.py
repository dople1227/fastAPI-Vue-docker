from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..auth.jwt_handler import create_access_token
from ..auth.hash_password import HashPassword
from ..database.connection import get_session
from ..models.users import User, TokenResponse
from sqlmodel import select


user_router = APIRouter(
    tags=["User"],
)
hash_password = HashPassword()


# 사용자 등록
@user_router.post("/signup")
async def sign_new_user(new_user: User, session=Depends(get_session)) -> dict:
    # 등록된 사용자인지 체크
    select_user_exist = select(User).where(User.email == new_user.email)
    results = session.exec(select_user_exist)
    user_exist = results.first()

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email exists",
        )

    # 등록된 사용자가 아니면 INSERT
    hashed_password = hash_password.create_hash(new_user.password)
    new_user.password = hashed_password
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "User created successfully."}


# 사용자 로그인
@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(
    user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)
) -> dict:
    # 등록된 사용자인지 체크
    select_user_exist = select(User).where(User.email == user.username)
    results = session.exec(select_user_exist)
    user_exist = results.first()

    # 유저가 존재하는지 체크
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )

    # 패스워드가 일치하는지 체크
    # if user_exist.password == user.password:
    #     return {"message": "User signed in successfully"}
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {"access_token": access_token, "token_type": "Bearer"}

    # 패스워드 불일치시 Exception 발생
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid details passed"
    )
