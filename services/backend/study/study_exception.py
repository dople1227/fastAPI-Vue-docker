# def print_exception():
# '''예외처리
# as err: err에 오류내용을 전달
# '''
#     short_list = [1, 2, 3]
#     while True:
#         value = input("Input Position [q to quit]?")
#         if value == "q":
#             break
#         try:
#             position = int(value)
#             print(short_list[position])
#         except ValueError as err:
#             print("ValueError Occur")
#             print(err)
#         except IndexError as err:
#             print("IndexError Occur")
#             print(err)
#         except Exception as err:
#             print("UnknownError Occur")
#             print(err)

# print_exception()


class CustemException(Exception):
    """커스텀예외 처리"""

    print("CustemException Occur")


words = ["eenie", "meenie", "miny", "MO"]
for word in words:
    if word.isupper():
        raise CustemException(word)
