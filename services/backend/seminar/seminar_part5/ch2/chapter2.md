# 2. OAuth2와 JWT를 사용한 애플리케이션 보안

###### 인증 흐름
![Alt text](img/diagram1.png)

#### 2.1 인증 기능 구조화
- 이벤트플래너 애플리케이션에 인증 기능을 추가하기 위해 폴더 및 파일추가

      planner/
          auth/
            jwt_handler.py
            authenticate.py
            hash_password.py
  - jwt_handler.py : JWT문자열을 인코딩 / 디코딩
  - authenticate.py : authenticate 의존 라이브러리가 포함되며 인증 및 권한을 위해 라우트에 주입된다.
  - hash_password.py : 패스워드를 암호화하는 함수가 포함된다. 계정을 등록하거나 로그인 시 패스워드 비교에 사용됨

#### 2.2 패스워드 해싱
- 데이터베이스 연결에서 사용자 패스워드를 일반텍스트로 저장했었는데 bcrypt를 사용해 암호화 해보자.

##### 2.2.1 passlib 라이브러리 설치
> (venv)$ pip install passlib[bcrypt]

<br/>

##### 2.2.2 패스워드를 해싱하는 함수 작성

###### /auth/hash_password.py
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

```

  - create_hash() : 문자열을 해싱한 값을 반환
  - verify_hash() : 일반 텍스트 패스워드와 해싱한 패스워드를 인수로 받아 두 값이 일치하는지 비교한다. 일치 여부에 따라 boolean값을 반환
  
<br/>

##### 2.2.3 패스워드 해싱한 값을 데이터베이스에 저장하도록 사용자등록 함수 변경

###### /routes/users.py
```python
# from ..auth.hash_password import HashPassword
from ..database.connection import Database 


user_database = Database(User)
# hash_password = HashPassword()

# 사용자 등록
@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already",
        )
    # hashed_password = hash_password.create_hash(user.password)
    # user.password = hashed_password
    await user_database.save(user)
    return {"message": "User successfully registered"}
```
