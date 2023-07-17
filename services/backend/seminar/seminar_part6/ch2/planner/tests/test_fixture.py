import pytest
from ..models.events import EventUpdate


# 픽스처 정의
@pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title="이벤트 업데이트 타이틀",
        image="https://업데이트이미지/fastapi.png",
        description="이벤트 설명 업데이트",
        tags=["테스트 1", "테스트 2", "테스트 3"],
        location="로케이션 업데이트",
    )


def test_event_name(event: EventUpdate) -> None:
    assert event.title == "이벤트 업데이트 타이틀"
