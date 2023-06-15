# set()
drinks = {
    "martini": {"vodka", "vermouth"},
    "black russian": {"vodka", "kahlua"},
    "white russian": {"cream", "kahlua", "vodka"},
    "manhattan": {"rye", "vermouth", "bitters"},
    "screwdriver": {"orange juice", "vodka"},
}

a = {1, 2}
b = {2, 3}

c = a & b
d = a.intersection(b)


# # 1.vodka가 포함된 음료만 추출
# for name, contents in drinks.items():
#     if "vodka" in contents:
#         print(name)

# # 2.vodka가 포함되었고 cream,vermouth가 없는 음료만 추출
# for name, contents in drinks.items():
#     if "vodka" in contents and not ("cream" in contents or "vermouth" in contents):
#         print(name)

# # 3. 2번을 set교집합 연산자인 &를 사용하여 간단히 작성
# # 둘다 존재하지 않는다면 false, 하나라도 존재하면 true
# for name, contents in drinks.items():
#     if "vodka" in contents and not contents & {"cream", "vermouth"}:
#         print(name)

bruss = drinks["black russian"]
wruss = drinks["white russian"]
bruss.update(["John", "Sam"])
bruss.discard("Johns")
bruss = bruss.union(wruss)

print(bruss)
