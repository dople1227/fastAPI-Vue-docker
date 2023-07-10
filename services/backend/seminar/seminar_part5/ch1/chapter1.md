- 애플리케이션 보안은 허가되지 않은 개체가 애플리케이션을 해킹하거나  
  불법적으로 변경하는 것을 방지하기 위해 애플리케이션에 대한 접근을 제한하는 것

  | 인증과 허가          | 설명                                           |
  | -------------------- | ---------------------------------------------- |
  | 인증(authentication) | 개체가 전달한 인증 정보를 검증하는 것          |
  | 허가(authorization)  | 개체가 특정 처리를 할 수 있도록 권한을 주는 것 |

- Part5 의 목표  
  - hash를 사용해 패스워드를 보호하고 FastAPI 애플리케이션에 인증 계층을 추가할 수 있다. 
  - 허가되지 않은 사용자로부터 라우트를 보호할 수 있다.

<br/>

#### 1.1 FastAPI의 주요 인증 방식
- 기본 HTTP 인증
  - 사용자 인증 정보(일반적으로 ID/PW)를 HTTP 요청 헤더에 인코딩하여 전송하는 간단한방식
  - HTTPBasic클래스를 사용하여 구현 가능

<br/>

- 쿠키 (Cookie)
  - 데이터를 클라이언트 측(웹 브라우저 등)에 저장할 때 사용
  - FastAPI 애플리케이션도 쿠키를 사용해서 사용자 정보를 저장할 수 있으며  
    서버는 이 정보를 추출해 인증 처리에 사용한다.

<br/>

- bearer 토큰 인증
  - bearer 토큰이라는 보안 토큰을 사용해 인증하는 방식
  - Bearer 키워드와 함께 요청의 Authorization 헤더에 포함돼 전송된다.
  - 가장 많이 사용되는 토큰은 JWT이며 사용자ID와 토큰 만료 기간으로  
    구성된 딕셔너리 형식이 일반적
  - Part 5에서는 bearer 토큰 인증을 다룬다.

<br/>

#### 1.1 의존성 주입
- 객체(함수)가 실행에 필요한 인스턴스 변수를 받는 방식
- FastAPI에서는 라우트 처리 함수의 인수로 의존 라이브러리를 주입한다.

```python
@user_router.post("/signup")
async def sign_new_user(new_user: User) -> dict:
    select_user_exist = select(User).where(User.email == new_user.email)
```
여기서 User 클래스가 의존 라이브러리이며 이를 sign_new_user()함수에 주입한다.
User를 사용자함수의 인수로 주입해 User객체의 인스턴스인 new_user를 생성하였으며 이를 통해 User 클래스의 속성을 쉽게 추출할 수 있다.

<br/>

#### 1.2 의존 라이브러리 생성
- FastAPI에서 의존 라이브러리는 함수 또는 클래스로 정의된다.
- 생성된 의존 라이브러리는 기본값과 메서드에 접근할 수 있으므로 함수 내에서 이러한 객체를 상속하지 않아도 된다.
- 의존성 주입은 반복된 코드 작성을 줄여주므로 인증과 허가처럼 반복적인 구현이 필요한 경우에 큰 도움이 됨  
  
다음과 같이 의존 라이브러리를 정의하고 사용할 수 있다.

###### 의존 라이브러리 정의
```python
async def get_user(token: str):
    user = decode_token(token)
    return user
```

###### 의존 라이브러리 사용
```python
from fastapi import Depends

@router.get("/user/me")
async get_user_details(user: User = Depends(get_user)):
  return user
```

- 이 라우트 함수는 get_user라는 함수에 의존한다.
- Depends 클래스는 라우트가 실행될 때 인수로 받은 함수를 실행하고 함수의 반환값을 라우트에 전달한다.