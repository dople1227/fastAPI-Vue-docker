# 2. pydantic 모델을 사용한 요청 바디 검증
## 2.1 pydantic이란?
- 타입 어노테이션을 사용해 데이터를 검증하는 파이썬 라이브러리
- 정의된 데이터만 전송되도록 요청바디를 검증할 수 있다.
- 요청 데이터가 적절한지 확인하고 악의적인 공격의 위험을 줄일수 있다.

### - model.py
```python
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str