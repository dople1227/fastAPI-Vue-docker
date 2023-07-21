import httpx
import pytest

import sys
from pathlib import Path
from planner.auth.jwt_handler import create_access_token
from planner.models.events import Event
from planner.database.connection import get_session_test
# from planner.tests.conftest import init_db
import pdb

ROOT_PATH = str(Path(__file__).resolve().parents[2])
sys.path.append(ROOT_PATH)


@pytest.fixture(scope="module")
async def access_token() -> str:
    return create_access_token("test@test.com")


@pytest.fixture(scope="module")
async def mock_event() -> Event:
    pdb.set_trace()   
    new_event = Event(
        creator="test@test.com",
        title="테스트이벤트",
        image="테스트이미지경로",
        description="테스트 설명",
        tags=["테스트 태그1", "테스트 태그2", "테스트 태그3"],
        location="테스트 로케이션",
    )

    # await init_db()
    session = get_session_test()

    # 이벤트 생성
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    yield new_event


@pytest.mark.asyncio
async def test_get_events(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    """
    모든 이벤트 조회 테스트
    GET /event
    """
    pdb.set_trace()   
    response = await default_client.get("/event")
    assert response.status_code == 200
    assert response.json()[0]["id"] == mock_event.id


@pytest.mark.asyncio
async def test_get_event(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    """
    단일 이벤트 조회 테스트
    GET /event/{id}
    """
    pdb.set_trace()   
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.get(url)
    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["id"] == mock_event.id


@pytest.mark.asyncio
async def test_post_event(default_client: httpx.AsyncClient, access_token: str) -> None:
    """
    이벤트 생성 테스트
    POST /event/new
    """
    payload = {
        "title": "테스트이벤트",
        "image": "테스트이미지경로",
        "description": "테스트 설명",
        "tags": ["테스트 태그1", "테스트 태그2", "테스트 태그3"],
        "location": "테스트 로케이션",
    }

    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    test_response = {"메시지": "이벤트가 생성되었습니다."}

    response = await default_client.post("/event/new", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_get_events_count(default_client: httpx.AsyncClient) -> None:
    """
    저장된 이벤트 개수 확인용 테스트

    mock_event 픽스처에서 이벤트 1개 생성
    test_post_event()에서 이벤트 1개 생성
    : 총 2개의 이벤트 생성
    """
    response = await default_client.get("/event")

    events = response.json()

    assert response.status_code == 200
    assert len(events) == 2


@pytest.mark.asyncio
async def test_update_event(
    default_client: httpx.AsyncClient, mock_event: Event, access_token: str
) -> None:
    """
    이벤트 변경 테스트
    """
    test_payload = {"title": "업데이트된 테스트이벤트"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"/event/{mock_event.id}"
    response = await default_client.put(url, json=test_payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == test_payload["title"]


@pytest.mark.asyncio
async def test_delete_event(
    default_client: httpx.AsyncClient, mock_event: Event, access_token: str
) -> None:
    """
    이벤트 삭제 테스트
    """
    test_response = {"메시지": "이벤트가 정상적으로 삭제되었습니다."}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"/event/{mock_event.id}"

    response = await default_client.delete(url, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_get_event_again(
    default_client: httpx.AsyncClient, mock_event: Event
) -> None:
    """이벤트 정상적으로 삭제되었는지 테스트
    이 테스트가 정상적으로 동작했다면 발생해야 하는 코드는 404 이다.
    데이터가 삭제되어 없어야 되기 때문이다.
    200은 오류, 404
    """
    pdb.set_trace()   
    url = f"/event/{mock_event.id}"
    response = await default_client.get(url)

    assert response.status_code == 404
    if response.status_code != 404:
        assert response.json()["creator"] == mock_event.creator
        assert response.json()["id"] == mock_event.id
