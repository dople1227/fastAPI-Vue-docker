from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .model import Base

# MySQL 연결 정보
host = "localhost"
# db_adapter = "asyncmy"
db_adapter = "pymysql"
port = 3306
username = "root"
password = "jhlee1324"
database_name = "soron"

# aiomysql 드라이버를 사용하여 DATABASE_URL 구성
DATABASE_URL = (
    f"mysql+{db_adapter}://{username}:{password}@{host}:{port}/{database_name}"
)


# create_async_engine() 함수로 엔진 생성
db_engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=db_engine)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


# 세션을 반환하는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
