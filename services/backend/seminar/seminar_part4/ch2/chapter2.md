# 2. DATABASE 생성 및 Event model추가
- SQLModel에서는 SQLAlchemy 엔진을 사용하여 데이터베이스를 연결한다.
- SQLAlchemy 엔진은 create_engine() 메서드를 사용해서 생성한다.
- create_engine() 메서드는 데이터베이스 URL을 인수로 사용한다.
  - sqlite:///database.db 또는 sqlite:///database.sqlite와 같은 형식    
- create_engine() 메서드는 연결에 필요한 설정이 준비된 Engine 객체만을 생성하며
  실제 서버에 연결하거나 데이터베이스를 생성하는 작업은 수행하지 않는다.
- 데이터베이스 연결 및 생성은 create_all(engine)메서드에서 수행한다.

```python
database_file = "database.db"
engine = create_engine(database_file, echo=True)
SQLModel.metadata.create_all(engine)
```

> 💡 create_engine()의 echo  
> echo를 true로 설정하면 실행되는 SQL명령을 콘솔에 출력한다.

- create_all() 메서드는 데이터베이스뿐만 아니라 테이블도 생성한다. 테이블 생성을 위해서는 데이터베이스 연결시 반드시 테이블 파일이 import되어야 한다.

<br/>

#### 2.1 이벤트플래너 애플리케이션에 데이터베이스 연동
  
##### 2.1.1 UPDATE처리용 검증 모델 추가

###### /models/events.py
```python
class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]] 
    location: Optional[str]
                       
    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "this is description",
                "tags": ["python","fastapi","book" ,"lunch"],
                "location": "Google Meet"
            }
        }
```

<br/>


#### 2.1.2 데이터베이스 연결파일 작성

###### /database/connection.py
```python
from sqlmodel import SQLModel, Session, create_engine


database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    database_connection_string, echo=True, connect_args=connect_args
)


def conn():
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session
```
<br/>

#### 2.1.3 main 실행 시 데이터베이스 연결

###### /database/main.py
```python
from fastapi import FastAPI
from .routes.users import user_router
from .routes.events import event_router
from .database.connection import conn


app = FastAPI()


@app.on_event("startup")
def on_startup():
    conn()


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
```

<br/>

###### 코드 작성 후 실행결과
![Alt text](img/part4_ch2_image.png)

- 데이터베이스 엔진 생성 시에 echo=True로 설정하면 위와같이 SQL명령이 출력된다.

