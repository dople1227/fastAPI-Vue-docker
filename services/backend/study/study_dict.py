"""딕셔너리 설명

zip() : 두개의 리스트를 딕셔너리로 합칠때 유용
할당(=), shallow copy(copy()), deep copy(copy.deepcopy(dict)) 차이
1.할당
copied_dict_list = dict_list
동일한 객체를 가리키며 둘 중 어느값을 변경해도 양쪽값이 함께 변경됨

2.shallow copy
copied_dict_list = dict_list.copy()
불변 데이터타입의 값 변경 시엔 한쪽 값만 변경되지만
가변 데이터타입의 값 변경 시엔 양쪽값이 함께 변경됨

3.deep copy
import copy
copied_dict_list = copy.deepcopy(dict_list)
불변,가변 데이터타입 상관없이 한쪽의 값만 변경 됨
"""
import copy

english = ["Monday", "Tuesday", "Wednesday"]
french = ["Lundi", "Mardi", "Mercredi"]
dict_list = dict(zip(english, french))
dict_list["Thursday"] = "Soronprfbs"
dict_list["Thursday"] = "Soron"

dict_list2 = {
    "Friday": "Juno",
    "Saturday": "LJH",
    "Sunday": "LEEJUNHO",
    "Thursday": "CHANGE by dict_list2",
    "week": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
}

dict_list3 = {"Sunday": "CHANGED BY dict_list3"}
dict_list = {**dict_list, **dict_list2}
# dict_list.update(dict_list2)
# dict_list.update(dict_list3)
# dict_list.pop("Sunday", "Saturday_")
# copied_dict_list = copy.deepcopy(dict_list)
# copied_dict_list = dict_list.copy()
copied_dict_list = dict_list[:]
copied_dict_list["week"][0] = "CHANGE Monday"

print(dict_list)

# for key, value in copied_dict_list.items():
#     print("key", key, "value", value)


# list_keys=[]
# list_values=[]
# for key, value in dict_list2.items():
#     list_keys.append(key)
#     list_values.append(value)
