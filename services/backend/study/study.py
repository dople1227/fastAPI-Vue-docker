# tmpInt1 = 1
# tmpInt2 = 1
# tmpStr1 = "a"
# tmpStr2 = "a"
# tmpList = []
# tmpTuple = ()
# if (tmpStr1 == tmpStr2) and (tmpInt1 == tmpInt2):
#     print('true')
# else:
#     print('false')

# vowels = "aeiou"
# vowel_list = ["a", "e", "i", "o", "u"]
# vowel_tuple = ("a", "e", "i")
# letter = "o"
# if letter in vowels:
#     print("letter", letter, "is vowels")
# else:
#     print("letter is not vowel")

# secret = 4
# guess = 7
# if guess < secret:
#     print("too low")
# elif guess == secret:
#     print("same")
# elif guess > secret:
#     print("too high")

# small = True
# green = False

# if small and green:
#     print("pea")
# elif small and green:
#     print("cherry")
# elif small and green:
#     ("pumpkin")
# elif small and green:
#     print("watermelon")

# a = "test"
# b = "plan"
# tmpStr = "test" "plan" + str(1)
# print(a, b)

# letters = "abcdefghijklmnopqrstuvwxyz"
# tasks = "python,C#,java,Ruby,Go"
# taskList = tasks.split(",")
# joinTask = ",".join(taskList)
# poem = """All that doth flow we cannot liquid game.

# """
# tmp = 0
# tmpBool = bool(tmp)
# print(type(taskList))
# print(type(joinTask))
# print(joinTask)
# print(poem[:1])

# print(poem.index("t"), end="")
# print(poem.rindex("t"))
# print(poem.count("t"))
# print(poem)
# print(poem.strip())
# print(poem.strip().strip("."))
# print(poem.center(30))

# thing = "wereduck"
# place = "werepond"
# salutation = "Sergent"
# name = "Juno"
# letter = f"Dear {salutation} {name}"

# print(letter)

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# number = [1, 2, 3, 4, 5]
# position = 0
# while position < len(number):
#     if number[position] % 2 == 0:
#         print("Found even number: ", number[position])
#         continue
#     position += 1
# else:
#     print("No even number found")

# numberList = [1, 2, 3, 4, 5]

# for number in numberList:
#     if number == 3:
#         continue
#     print(number)
# else:
#     print("else phrase")

# strTuple = (
#     "1",
#     "2",
#     "3",
# )
# print(strTuple)

# t1 = ("Fee", "Fie", "Foe")
# t2 = ("Flop",)
# print(id(t1), t1)
# t1 += t2
# print(id(t1), t1)
# l1 = ["Fee", "Fie", "Foe"]
# l2 = ["Glop", "Glich"]
# l3 = ["A1", "B2", "A3", "D4", "45"]
# l4 = l3
# l3copied = l3.copy()

# print(l3)
# str1 = "abcdefg"
# print(id(str1))
# str1 = str1.replace("c", "C")
# print(id(str1))
# print(str1)

# print(id(l1), l1)
# l1 += l2
# print(id(l1), l1)
# import copy

# a = [1, 2, [8, 9]]
# b = copy.deepcopy(a)
# c = list(a)
# d = a[:]

# a[2][1] = "changed!"
# for item in b:
#     if type(item) != list:
#         print(item)
#         continue
#     for jtem in b[2]:
#         print("inner list:", jtem)

# days = ["Monday", "Tuesday", "Wednesday"]
# fruits = ["banana", "apple", "orange"]
# drinks = ["coffee", "tea", "coke"]
# desserts = ["tiramisu", "ice cream", "pie", "pudding"]

# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(f"day: {day}, fruit: {fruit}, drink: {drink}, dessert: {dessert}")


# number_list = [number for number in range(1, 9)]
# print(number_list)
# even_list = [number for number in number_list if number % 2 == 0]
# print(even_list)

# rows = range(1, 4)
# cols = range(1, 3)
# for row in rows:
#     for col in cols:
#         print(row, col)

# cells = [(row, col) for row in rows for col in cols]
# for cell in cells:
#     print(cell)
