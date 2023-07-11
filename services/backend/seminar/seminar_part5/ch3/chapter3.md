# 3. 이벤트플래너 애플리케이션에 인증모델 적용

#### 3.1 로그인 라우트 변경

###### /routes/users.py
```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..auth.jwt_handler import create_access_token

async def sign_user_in(user: OAuth2Pass)
```