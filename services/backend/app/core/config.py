# DATABASE_URL 구성 정보
host = "localhost"
# db_adapter = "asyncmy"
db_adapter = "pymysql"
port = 3306
username = "root"
password = "jhlee1324"
database_name = "soron"
DATABASE_URL = (
    f"mysql+{db_adapter}://{username}:{password}@{host}:{port}/{database_name}"
)
