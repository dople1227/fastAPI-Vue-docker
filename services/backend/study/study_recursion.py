def flatten(lol):
    """재귀함수
    리스트의 리스트와 같이 '고르지않은' 데이터를 처리할 때 유용
    """
    for item in lol:
        if isinstance(item, (list, tuple, set)):
            # for subitem in flatten(item):
            #     yield subitem
            # 파이썬 3.3부터 yield from 으로 대체 가능
            yield from flatten(item)
        else:
            yield item


lol = [
    1,
    2,
    (3, 4, 5),
    [6, [7, {8, 9}], [{"name": "Lee", "age": 20}, {"name": "John", "age": 30}]],
]

print((tuple(flatten(lol))))
