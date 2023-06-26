# 2. FastAPI 애플리케이션 구조화

> 💡 구조화란?
>
> 소스코드와 리소스를 구조적으로 조직화 하는것
> 
> 코드의 가독성,유지보수성,재사용성,테스트 용이성 등을 향상시켜 전체적인 생산성을 높임

- 이벤트 플래너를 만들어 보자
- 아래와 같은 구조로 설계한다.
        
        planner/
            main.py
            database/
                connection.py
            routes/
                events.py
                users.py
            models/
                events.py
                users.py

  - database 폴더
    - connection.py : 데이터베이스 추상화와 설정에 사용되는 파일
  - routes 폴더 
    - events.py : 이벤트 생성,변경, 삭제 등의 처리를 위한 라우팅
    - users.py : 사용자 등록 및 로그인 처리를 위한 라우팅
  - models 폴더
    - events.py : 이벤트 처리용 모델을 정의
    - users.py : 사용자 처리용 모델을 정의
