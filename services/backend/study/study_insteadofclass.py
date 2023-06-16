# === namedtuple
# 불변 객체처럼 행동
# 객체보다 공간효율성, 시간효율성이 좋음
# 딕셔너리 형식의 대괄호([]) 대신, 온점(.) 표기법으로 속성 접근 가능
# 네임드 튜플을 딕셔너리의 키처럼 사용 가능

# from collections import namedtuple

# Duck = namedtuple("Duck", "bill,tail")
# # duck = Duck("wide orange", "long")

# parts = {"bill": "wide orange", "tail": "long"}
# duck = Duck(**parts)

# print(type(duck.bill), duck.bill)


# === 데이터 클래스
# @dataclass로 사용
# 간단하게 데이터 컬렉션 생성


from dataclasses import dataclass


@dataclass
class AnimalClass:
    type: str
    name: str
    teeth: int = 0


animal = AnimalClass("Human", "Jhon")
animal.name = "Grace"
print(type(animal), animal)

# attrs
# https://www.attrs.org/en/stable/
# 내부 라이브러리보다 좋은지 비교
