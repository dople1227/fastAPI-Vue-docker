# 4. 몽고DB 설정
- FastAPI와 몽고DB를 연결해주기 위해 beanie를 사용
> (venv) $ pip install beanie==1.13.1
#### 4.1 문서
- 몽고DB는 NoSQL(Not Only SQL)데이터베이스로 비관계형 데이터베이스
- NoSQL 데이터베이스에서는 데이터 저장을 위해 문서를 사용한다. pydantic 스키마와 동일한 방식으로 정의되며 유일한 차이점은 beanie가 제공하는 Document 클래스를 사용한다는 점이다.

    ```python
    from beanie import Document

    class Event(Document):
        name: str
        location: str

        class Settings:
            name = "events"
    ```
- 여기서 Settings 서브클래스는 몽고DB 데이터베이스 내에 설정한 이름으로 컬렉션을 생성한다.
- 문서 생성방법을 알았으니 CRUD 처리를 위한 메서드를 살펴보자.

<br/>

##### 4.1.1 CRUD 처리를 위해 beanie가 제공하는 메서드
  - insert(), create(): 문서 인스턴스에 의해 호출되며 데이터베이스 내에 새로운 레코드를 생성한다. 단일 데이터는 insert_one()메서드를 사용해 추가하고 여러 개의 데이터는 insert_many()메서드를 사용해 추가한다.
    ```python
    event1 = Event(name="Packt office launch", location="Hybrid")
    event2 = Event(name="Hanbit office launch", location="Hybrid")
    await event1.create()
    await event2.create()
    await Event.insert_many([event1, event2])
    ```

<br/>

- find(), get(): find()메서드는 문서 목록에서 인수로 지정한 문서를 찾는다.  
  get()메서드는 지정한 ID와 일치하는 단일 문서를 반환한다.find_one()메서드는
  다음과 같이 지정한 조건과 일치하는 단일 문서를 반환한다.
    ```python
    # ID와 일치하는 단일 문서를 반환한다.
    event = await Event.get("74478287284ff")
    # 일치하는 아이템의 리스트를 반환한다.
    event = await Event.find(Event.location == "Hybrid").to_list()
    # 단일 이벤트를 반환한다.
    event = await.find_one(Event.location == "Hybrid")
    ```

<br/>

- save(), update(), upsert(): save()메서드는 데이터를 신규 문서로 저장할 때 사용된다. update()는 기존 문서를 변경할 때 사용되고, upsert()는 조건에 부합하는 문서가 있다면 update(), 없으면 save()로 사용된다 (insert+update의 합성어)
    ```python
    event = await Event.get("74478287284ff")
    update_query = {"$set": {"location": "virtual"}}
    await event.update(update_query)
    ```

<br/>

- delete(): 데이터베이스에서 문서를 삭제한다. 
    ```python
    event = await Event.get("74478287284ff")
    await event.delete()
    ```

<br/>

#### 4.2 데이터베이스 초기화
- 이벤트 플래너 애플리케이션에 몽고DB를 설정하고 문서를 정의하자.
- 아래 순서로 진행한다.

<br/>

##### 4.2.1 데이터베이스 연결

###### /database/connection.py
```python
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings
from ..models.users import User
from ..models.events import Event


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(), document_models=[Event, User]
        )

    class Config:
        env_file = ".env"

```

<br/>

##### 4.2.2 이벤트 모델

###### /models/events.py
```python
from beanie import Document
from typing import Optional, List
from pydantic import BaseModel


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "This is description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
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
                "description": "This is Description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }
```

<br/>

##### 4.2.4 사용자 모델

###### /models/users.py
```python
from typing import Optional, List
from beanie import Document
from pydantic import BaseModel, EmailStr
from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "jhlee@yescnc.co.kr",
                "username": "juno",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
```

<br/>

##### 4.2.6 환경파일 (.env)생성

###### /.env
```
DATABASE_URL = mongodb://localhost:27017/planner
```