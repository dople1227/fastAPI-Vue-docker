#### 2. 테스트 환경 구축
- CRUD 처리용 라우트와 사용자 인증을 테스트 해본다.


2.1 비동기 API를 테스트하기 위해 pytest-asyncio를 설치한다.
> (venv)$ pip install pytest-asyncio

<br/>

2.2 설치가 완료됐으면 pytest.ini 설정 파일을 생성한다. pytest.ini파일은 pytest명령을 실행할 경로 혹은 하위 디렉토리에 있어야 한다.  
pytest가 실행될 때 위 ini 파일의 내용을 설정하여 실행하게 된다.

    ###### /planner/pytest.ini
    ```ini
    [pytest]
    asyncio_mode = auto
    ```
- asyncio_mode = auto는 모든 테스트를 비동기식으로 실행한다는 의미이다.

<br/>

2.3 테스트 시작점이 될 conftest.py파일을 tests폴더내에 생성한다.

> 💡 conftest.py  
> pytest에서 사용되는 픽스처, 훅, 설정 등을 정의할 수 있는 파일  
> conftest가 존재하는 경로 및 하위 디렉터리에 영향을 줄 수 있다.  
> conftest에서 정의한 픽스처는 해당 디렉터리와 하위 디렉터리에서 실행되는 모든 테스트에서 사용할 수 있다.

<br/>

###### /tests/conftest.py
```python
import asyncio
import httpx
import pytest

from ..main import app
from ..database.connection import Settings
from ..models.events import Event
from ..models.users import User

@pytest.fixture(scope="session")
def event_loop():
    
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
```

- asyncio모듈: 활성 루프 세션을 만들어서 테스트가 단일스레드로 실행되도록 한다.
- httpx모듈: HTTP CRUD 처리를 실행하기 위한 비동기 클라이언트 역할. 비동기 요청을 만들고 보낼 수 있다.
- pytest: 픽스처 정의를 위해 사용


> 💡 fixture의 scope  
> scope 파라미터는 픽스처 함수의 유효범위를 지정할 때 사용한다.  
> 아래는 scope에서 사용 가능한 값들이다.

###### fixture의 scope에 사용되는 값
|     | 이름     | 설명                                                                                                                                                                                 |
| --- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|     | session  | 세션 내에서 픽스처 함수가 한번 실행되고, 해당 픽스처를 사용하는 모든 테스트함수에서 fixture객체를 공유한다. 여기서 세션이란 pytest를 실행하고 종료되기까지의 시간을 말한다.          |
|     | module   | 모듈내에서 픽스처 함수가 한번 실행되고, 해당 픽스처를 사용하는 같은 모듈에 있는 모든 테스트함수에서 fixture 객체를 공유한다. 여기서 모듈이란 테스트를 진행하는 파이썬 파일을 말한다. |
|     | class    | 클래스내에서 픽스처 함수가 한번 실행되고, 해당 픽스처를 사용하는 같은 클래스에 있는 모든 테스트함수에서 fixture 객체를 공유한다.                                                     |
|     | function | scope를 지정해주지 않았을때의 기본값. 픽스처를 사용하는 테스트 함수마다 새로 호출되며 객체를 공유하지 않는다.                                                                        |

<br/>

> 💡 event_loop 픽스처에 대해
> 픽스처를 사용하려면 테스트함수의 파라미터로 전달하여 사용하여야 하지만 event_loop픽스처는 테스트함수에서 직접 사용하지 않는다.  

2.4 기본 클라이언트 픽스처인 default_client픽스처를 작성한다.  
default_client는 httpx를 통해 비동기로 실행되는 애플리케이션 인스턴스를 반환하고 테스트를 위해 생성한 데이터들을 삭제한다.
    - 사용자이메일: test@test.com
    - 이벤트명: 테스트이벤트, 업데이트된 테스트이벤트(업데이트 테스트 시)
###### tests/conftest.py
```python
@pytest.fixture(scope="session")
async def default_client():    
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:        
        yield client
        
        # httpx 요청작업 완료 후 리소스 정리코드
        session = get_session()

        for _session in session:
            # 사용자 생성 테스트데이터 삭제
            sel_user = select(User).where(User.email == "test@test.com")
            sel_user_results = _session.exec(sel_user).fetchall()
            for user in sel_user_results:
                _session.delete(user)

            # 이벤트 생성 테스트데이터 삭제
            sel_event = select(Event).where(
                or_(Event.title == "테스트이벤트", Event.title == "업데이트된 테스트이벤트")
            )
            sel_event_results = _session.exec(sel_event)
            for event in sel_event_results:
                _session.delete(event)
            
            _session.commit()
            _session.close()
```
