import json
import datetime

utc_time = datetime.datetime.utcnow()
now = utc_time + datetime.timedelta(hours=9)


menu = {
    "breakfast": {
        "hours": "7-9",
        "items": {"breakfast menu1": "$6.00", "breakfast menu2": "$4.00"},
    },
    "lunch": {"hours": "12-14", "items": {"lunch menu1": "$8.00"}},
    "dinner": {"hours": "18-20", "items": {"dinner menu1": "$12.00"}},
}

json_dump = json.dumps(now, default=str)
menu_dump = json.dumps(menu, default=str)
menu_dict = json.loads(menu_dump)
# print(menu_dict)

list_keys = []
list_values = []
for key, value in menu_dict.items():
    list_keys.append(key)
    list_values.append(value)


# print(list_keys)
print(list_values)

str1 = "test"
str2 = "test"
copied_str1 = str1
str1 = "changed str"

print("str id:", id(str1), "str2 id:", id(str2), "copied str1 id:", id(copied_str1))
