# 1. SQLModel 
  - FastAPI 개발자가 만들었으며 pydantic과 SQLAlchemy를 기반으로 하는 ORM(Object-Relational Mapping)
  - 내장 모듈이 아니기에 따로 설치 해줘야 한다.
    >(venv)$ pip install sqlmodel 

> 💡 ORM이란?  
> 프로그래밍 코드로 생성한 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것.  
> SQL을 사용하지 않고도 객체를 통해 데이터베이스를 다룰 수 있게 해준다.

<br/>

#### 1.1 테이블
- SQLModel을 사용해서 테이블을 생성하려면 테이블 모델 클래스를 먼저 정의해야 한다.
- pydantic 모델 클래스처럼 정의하지만 SQLModel의 서브클래스로 정의해야 한다.
- table이라는 설정 변수를 가지며 이 변수를 통해 해당 클래스가 SQLModel 테이블 이라는 것을 인식한다.
- 모델 클래스 안에 정의된 변수는 따로 지정하지 않으면 기본 필드로 설정된다. (사용 시 기본값을 반드시 제공해줘야하며 그렇지 않을 시 validationError발생)

##### 1.1.1 Event테이블 모델 정의
###### /models/events.py
```python
from sqlmodel import SQLModel, JSON, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book",
                "image": "http://limktomyimage.com/image.png",
                "description": "this is description",
                "location": "Google Meet",
                "tags": ["python", "fastapi", "book", "launch"],
            }
        }
```

<br/>

> 💡 id의 자동증가값 다루기  
> id는 PK이기 때문에 DB상에서 NULL이 될 수 없다.
> 그럼에도 default=None으로 선언한 이유는 자동증가값은 DB를 참조하기전 파이썬코드상에서 id를 설정하지 않기 때문이고 이게 default=None으로 선언하는 유일한 이유이다.
> https://sqlmodel.tiangolo.com/tutorial/automatic-id-none-refresh/#automatic-ids-none-defaults-and-refreshing-data

<br/>

> 💡 arbitrary_types_allowd  
> 파이썬의 JSON인코더인 json.JSONEncoder 클래스의 속성.  
> 기본적으로 JSONEncoder는 직렬화 할 수 있는 데이터 유형에 제한을 둔다.  
> (str, int, float, list, dict, None 등)
>  
> arbitrary_types_allowed 값을 True 로 설정하면 제한된 기본 데이터 유형만이 아닌 사용자 정의 객체나 기타 Python 객체도 JSON으로 직렬화 할 수 있도록 해준다.

<br/>

#### 1.2 로우
- 로우에 데이터를 추가하고 저장하려면 테이블의 인스턴스를 만든 후 인스턴스의 변수에 원하는 데이터를 할당해야 한다. 다음은 하나의 이벤트 데이터를 이벤트 테이블에 추가하는 예시이다.

```python
new_event = Event(title="Book Launch",
                  image="src/fastapi.png", 
                  description="description..blahblah",
                  location="Google Meet",
                  tags=["packt", "book"])

with Session(engine) as session:
  session.add(new_event)
  session.commit()
```

<br/>

#### 1.3 세션
- 세션 객체는 코드와 데이터베이스 사이에서 이루어지는 처리를 관리하며 주로 특정 처리를 데이터베이스에 적용하기 위해 사용된다.
- Session 클래스는 SQL 엔진의 인스턴스를 인수로 사용한다.
- Session 클래스의 메서드
  - add() : 처리 대기중인 데이터베이스 객체를 메모리에 추가한다. 앞서 살펴본 코드에서 
    new_event 객체는 세션 메모리에 추가되고 commit() 메서드에 의해 데이터베이스에 실제로 반영된다.
  - commit() : 현재 세션에 있는 트랜잭션을 실제 데이터베이스에 모두 반영한다.
  - get() : 데이터베이스에서 단일 로우를 추출한다. 모델과 pk값인 id를 사용한다.

<br/>