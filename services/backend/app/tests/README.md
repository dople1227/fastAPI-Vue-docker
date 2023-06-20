== 테스트 실행법
pytest -s -v tests/test.py
-s : print() 등의 디버깅 출력문도 표시
-v : 실행된 함수명 포함 등 결과를 자세하게 표시

== conftest.py
테스트마다 공통적으로 적용될 부분을 fixture로 작성