#### 1.2 테스트 환경 구축
- CRUD 처리용 라우트와 사용자 인증을 테스트 해본다.

1. 비동기 API를 테스트하기 위해 pytest-asyncio를 설치한다.
    > (venv)$ pip install pytest-asyncio

2. 설치가 완료됐으면 pytest.ini 설정 파일을 생성한다. main.py가 있는 루트폴더에 생성 후 아래와 같이 코드를 추가한다.
- pytest가 실행될 때 위 ini 파일의 내용을 불러온다.

    ###### /planner/pytest.ini
    ```ini
    [pytest]
    asyncio_mode = auto
    ```
- 위 ini의 내용은 pytest가 모든 테스트를 비동기식으로 실행한다는 의미이다.

3. 테스트 시작점이 될 conftest.py파일을 tests폴더에 생성한다.

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
- httpx모듈: HTTP CRUD 처리를 실행하기 위한 비동기 클라이언트 역할
- pytest: 픽스처 정의를 위해 사용

4. 테스트를 위해 testdb를 사용한다.

