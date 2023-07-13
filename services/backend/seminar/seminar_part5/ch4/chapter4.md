# 4. CORS 설정

#### 4.1 CORS

> 💡 CORS란?  
> 
> 등록되지 않은 사용자가 리소스를 사용하지 못하도록 제한하는 규칙
> 특정 클라이언트에서 우리가 만든 API를 호출하면 브라우저가 호출의 출처(도메인)를 확인하여 제한한다.
> API와 출처(도메인)가 동일한 경우 또는 API에서 허가한 출처만 리소스에 접근할 수 있다.

<br/>

- FastAPI는 CORSMiddleware라는 미들웨어를 통해 API에 접근 가능한 도메인을 관리한다.
- CORSMiddleware는 서버의 리소스에 접근할 수 있는 도메인 목록을 배열로 관리한다.
- 예를 들어 특정 웹 사이트에서만 API에 접근할 수 있게 하려면 origins배열에 해당 URL을 추가하면 된다

###### test.com도메인 에서만 API를 허용하도록 설정
```python
origins = [
    "http://test.com",
    "https://test.com"
]
```

<br/>

- 모든 요청을 허용하도록 하려면 아래와 같이 설정해 주면 된다.
```python
origins = ["*"]
```

<br/>

- main.py를 수정하여 모든 도메인에서의 요청을 허가하도록 변경해보자.

###### main.py
```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS미들웨어설정
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headears=["*"],
)
```

