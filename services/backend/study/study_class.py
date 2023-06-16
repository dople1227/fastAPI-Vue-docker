# ====== 상속 ======
# class Person:
#     """__init__

#     객체 생성후에 실행되기에 생성자 개념이 아닌
#     초기화 하는 개념
#     """

#     def __init__(self, name="DefaultName"):
#         self.name = name

#     def exclaim(self):
#         print("I'm a Person Class")

#     pass


# class EmailPerson(Person):
#     """상속
#     class subClassName(SuperClassName)의 형태로 사용
#     issubclass(EmailPerson,Person) -> bool
#     super(): 슈퍼클래스를 얻어옴 super().__init__->Person._init__()
#     """

#     def __init__(self, name, email):
#         super().__init__(name)
#         self.email = email

#     def exclaim(self):
#         super().exclaim()


# personInstance = Person()
# emailpersonInstance = EmailPerson("EmailPersonName", "emailPerson@gmail.com")

# print(personInstance.name)
# print(emailpersonInstance.name)
# print(emailpersonInstance.email)


# # ====== 다중 상속 ======
# # 메서드나 속성을 찾을 때 실행순서 (Mule기준)
# # Mule.mro()
# # 1.객체 자신(Mule타입)
# # 2.객체의 클래스(Mule)
# # 3.클래스의 첫번째 부모 클래스(Donkey)
# # 4.클래스의 두번째 부모 클래시(Horse)
# # 5.부모의 부모 클래스(Animal)
# class Animal:
#     mem1 = 14

#     def says(self):
#         return "Animal"


# class Horse(Animal):
#     def says(self):
#         return "Horse"


# class Donkey(Animal):
#     def says(self):
#         return "Donkey"


# class Mule(Donkey, Horse):
#     mem1 = "mule"
#     pass


# class Hinny(Horse, Donkey):
#     pass


# mule = Mule()
# print(mule.mem1)


# 믹스인
# 코드재사용과 기능 모듈화를 위한 디자인 패턴
# 타 클래스에 특정 기능을 제공하기 위해 사용되는 작은단위의 클래스
# 클래스명 마지막에 Mixin을 붙임 (self처럼 관례)
# 믹스인 클래스
# class PrintableMixin:

#     def print_info(self):
#         print("Info:", self.info)


# # 주요 클래스
# class Book(PrintableMixin):
#     def __init__(self, title, author, info):
#         self.title = title
#         self.author = author
#         self.info = info


# class Movie(PrintableMixin):
#     def __init__(self, title, director, info):
#         self.title = title
#         self.director = director
#         self.info = info


# # 객체 생성
# book = Book("Harry Potter", "J.K. Rowling", "Fantasy novel")
# movie = Movie("Inception", "Christopher Nolan", "Sci-fi thriller")

# # 믹스인의 메서드 호출
# book.print_info()  # Info: Fantasy novel
# movie.print_info()  # Info: Sci-fi thriller


# === 속성접근 ===
# private: getter, setter로 속성에 직접 접근할 수 없도록 작성
# property()를 이용해 직접접근도 가능하도록 설정가능
# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name

#     def get_name(self):
#         print("inside the getter")
#         return self.hidden_name

#     def set_name(self, input_name):
#         print("inside the setter")
#         self.hidden_name = input_name

#     name = property(fset=set_name, fget=get_name)


# don = Duck("Donald")
# # Getter, Setter로만 접근가능
# print(don.get_name())
# don.set_name("Arnold")
# print(don.get_name())

# # Getter, Setter와 property()를 이용하여 직접접근도 가능
# print(don.name)
# don.name = "Michael"
# print(don.name)


# # === 데코레이터를 이용한 접근 ===
# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name

#     @property
#     def name(self):
#         print("inside of getter")
#         return self.hidden_name

#     @name.setter
#     def name(self, input_name):
#         print("inside the setter")
#         self.hidden_name = input_name


# fowl = Duck("Donald")
# print(fowl.name)
# fowl.name = "Howard"
# print(fowl.name)


# @property 사용한 읽기전용 계산값
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def diameter(self):
#         return 2 * self.radius


# c = Circle(5)
# c.radius = 4
# print(c.diameter)


# # === 프라이버시를 위한 네임 맹글링 (__name속성에 바로 접근 불가)
# class Duck:
#     def __init__(self, input_name):
#         self.__name = input_name

#     @property
#     def name(self):
#         print("inside the getter: ", self.__name)
#         return self.__name

#     @name.setter
#     def name(self, input_name):
#         print("inside the setter")

#         self.__name = input_name


# fowl = Duck("Donald")
# fowl.name
# fowl.name = "Howard"


# # === 덕타이핑 ===
# class Quote:
#     def __init__(self, person, words):
#         self.person = person
#         self.words = words

#     def who(self):
#         return self.person

#     def says(self):
#         return self.words + ","


# class QuestionQUote(Quote):
#     def says(self):
#         return self.words + "?"


# class ExclamationQuote(Quote):
#     def says(self):
#         return self.words + "!"


# hunter = Quote("Quote", "Quote word")
# # print(hunter.who(), "says:", hunter.says())

# hunter1 = QuestionQUote("Question", "Question word")
# # print(hunter1.who(), "says:", hunter1.says())

# hunter2 = ExclamationQuote("Exclamation", "Exclamation word")
# # print(hunter2.who(), "says:", hunter2.says())


# class BabblingBrook:
#     def who(self):
#         return "Brook"

#     def says(self):
#         return "Brook word"


# brook = BabblingBrook()


# def who_says(obj):
#     print(obj.who(), "says", obj.says())


# who_says(hunter)
