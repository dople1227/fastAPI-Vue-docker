from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    """패스워드 해싱 함수. bcrypt를 사용하여 해싱
    - create_hash(): 문자열로 된 패스워드를 bcrypt로 해싱한 후 해싱된 문자열 return
    - verify_hash(): 해싱되기 전 문자열과 해싱된 후의 문자열을 입력받아 같은 값인지 비교
    """

    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)
