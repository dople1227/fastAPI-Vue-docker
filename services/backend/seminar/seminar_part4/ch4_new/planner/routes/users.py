from fastapi import APIRouter, HTTPException, status, Depends
from ..models.users import User, UserSignIn
from ..database.connection import get_session
from sqlmodel import select

user_router = APIRouter(
    tags=["User"],
)


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
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "User created successfully."}


# 사용자 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn, session=Depends(get_session)) -> dict:
    # 등록된 사용자인지 체크
    select_user_exist = select(User).where(User.email == user.email)
    results = session.exec(select_user_exist)
    user_exist = results.first()

    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )

    # 패스워드가 일치하는지 체크
    if user_exist.password == user.password:
        return {"message": "User signed in successfully"}

    # 패스워드 불일치시 Exception 발생
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
    )
