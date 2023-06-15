# def whatis(thing):
""" None과 false는 다르다는걸 확인하는 예
"""
#     if thing is None:
#         print(thing, "is None")
#     elif thing:
#         print(thing, "is True")
#     else:
#         print(thing, "is False")


# def menu(wine, entree="rice", dessert="icecrean"):
""" 위치인수, 키워드인수, 기본값지정 예

- 인수 순서는 (위치인수, 위치인수...,키워드 인수...,)
- 위치인수: 기본적인 함수 인수. 위치로 할당
- 키워드인수: 인수 순서와 상관없이 정의된 인수이름으로 할당
- 기본값지정: 생략가능하며 생략 시 기본값이 할당.
    기본값은 처음 한번만 할당 됨.
"""
#     return {"wine": wine, "entree": entree, "dessert": dessert}
# print(menu("Wine1", dessert="icecream", entree="rice"))
# print(menu("Wine1", "icecrem", "rice"))


# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)

# buggy("a", ["테스트"])
# buggy("b")
# buggy("a", ["테스트"])
# buggy("b")


# def print_arguments(*args, **kwargs):
#     """*args, **kwargs (함수정의 시)

#     *args: 가변 위치 매개변수. 함수내에서 args라는 하나의 위치 매개변수로 모아서 사용
#     *kwargs: 가변 키워드 매개변수. 함수내에서 kwargs라는 하나의 키워드 매개변수로 모아서 사용
#     """
#     print("가변 위치 매개변수:")
#     for arg in args:
#         print(arg)

#     print("가변 키워드 매개변수:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_arguments("Alice", "Bob", name="Charlie", age=25)


# def print_info(name, age, location):
#     """*args, **kwargs (호출 시)

#     *args: 가변 위치 인수. 함수 호출시에 args라는 하나의 위치 매개변수로 모아서 호출하면
#         함수 내부에서 위치 매개변수로 풀어서 사용
#     *kwargs: 가변 키워드 인수. 함수 호출시에 kwargs라는 하나의 키워드 매개변수로 모아서 호출하면
#         함수 내부에서 키워드 매개변수로 풀어서 사용
#     """
#     print(f"이름: {name}", end=" | ")
#     print(f"나이: {age}", end=" | ")
#     print(f"위치: {location}")


# info_tuple = ("Alice", 25, "서울")
# info_tuple = ("p1", "p2", "p3")
# info_dict = {"name": "Bob", "age": 30, "location": "부산"}
# print_info(*info_tuple)
# print_info(**info_dict)
# print(print_info.__doc__)

# def print_data(data, *, start, end=100):
#     """키워드 전용 인수 사용법

#     * 이후에 이름:값으로만 호출할 매개변수들 정의
#     """
#     for value in data[start:end]:
#         print(value)


# data = ["a", "b", "c", "d", "e", "f"]
# print_data(data, end=6)


# def sum_args(*args):
#     return sum(args)


# def run_with_positional_args(func, *args):
#     return func(*args)


# print(run_with_positional_args(sum_args, 3, 4, 8, 2))
# print(sum_args(3, 4))


# def outer(a, b):
"""내부함수

함수 내에서 코드중복을 줄이기 위해 내부함수 사용. 외부함수가 종료되면 외부함수의 값에 접근불가.
"""
#     def inner(c, d):
#         return c + d
#     return inner(a, b)

# print(outer(5, 3))


# def outer_function(x):
"""클로저

내부함수와 비슷하나 외부함수가 종료된 후에도 외부함수의 값에 접근 가능.
"""
#     def inner_function(y):
#         return x + y
#     return inner_function

# add_five = outer_function(5)
# result = add_five(3)
# print(result)  # 출력: 8

# def document_it(func):
#     """데코레이터
#     """
#     def new_function(*args, **kwargs):
#         print("Running function:", func.__name__)
#         print("Positional arguments:", args)
#         print("Keyword arguments:", kwargs)
#         result = func(*args, **kwargs)
#         print("Result:", result)
#         return result
#     return new_function


# 1번과 2번은 동일
# == 1. ==
# def add_ints(a, b):
#     return a + b
# cooler_add_ints = document_it(add_ints)
# cooler_add_ints(3, 5)

# == 2. ==
# @document_it
# def add_ints(a, b):
#     return a + b
# add_ints(3, 5)

animal = "fruitbat"


def change_and_print_global():
    print("inside change_and_print_global:", animal)
    animal = "wombat"
    print("after the change:", animal)


def change_local():
    animal = "wombat"
    print("inside change_local:", animal, id(animal))


change_and_print_global()
# change_local()
