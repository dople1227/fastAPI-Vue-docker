from fastapi import APIRouter, HTTPException, status
from ..models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)
users = {}


# 사용자 등록
@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email exists",
        )
    users[data.email] = data
    return {"message": "User successfully registered"}


# 사용자 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully"}


# 사용자 리스트 가져오기
@user_router.get("/list")
async def get_user_list() -> dict:
    return {"users": users}
