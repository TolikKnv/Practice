# from decimal import Decimal, getcontext

# # 3
# getcontext().prec = 5
# numbers = {
#     'двадцать':20,
#     'тридцать':30,
#     'сорок':40,
#     'пятьдесят':50,
#     'два':2,
#     'три':3,
#     'четыре':4,
#     'пять':5
# }
# str_ = input()
# su = Decimal('0')
# for i in str_.split():
#     su+=numbers[i]

# print(su)
# print(Decimal(str(su**Decimal('0.5'))))


# 9
phones_list = [
    {"name": "Ivan", "city": "Moscow", "phones": ["232-19-55", "+7 (916) 230-00-75"]},
    {"name": "Anna", "city": "Samara", "phones": ["200-11-15"]},
    {"name": "Anna", "city": "Vologda", "phones": ["+7 (931) 711-00-75"]},
    {
        "name": "Nikolay",
        "city": "Moscow",
        "phones": ["+7 (916) 778-71-05", "331-66-11", "783-33-85"],
    },
    {"name": "Ivan", "city": "Moscow", "phones": ["+7 (916) 205-41-05", "232-19-55"]},
    {"name": "Anna", "city": "Samara", "phones": ["+7 (916) 105-13-56"]},
]

for i in range(len(phones_list)-1):
    for j in range(i+1, len(phones_list)):
        if phones_list[i]['name']==phones_list[j]['name'] and phones_list[i]['city']==phones_list[j]['city']:
            for item in phones_list[j]['phones']:
                if item not in phones_list[i]['phones']:
                    phones_list[i]['phones'].append(item)


p_l = phones_list.copy()
con = []
for i in range(len(p_l)-1):
    for j in range(i+1,len(p_l)):
        if p_l[i]['name']==p_l[j]['name'] and p_l[i]['city']==p_l[j]['city'] :
            continue
        else:
            con.append(p_l[i])
            break

for i in range(len(con)-1):
    for j in range(i+1,len(con)):
        if con[i]['name']==con[j]['name'] and con[i]['city']==con[j]['city'] :
            con.pop(j)

print(*con,sep = '\n')
print()
#9.2
merged = {}
for record in con:
    key = (record['city'], record['name'])
    merged.setdefault(key, set()).update(record['phones'])


result = {}
for (city, name), phones in merged.items():
    result.setdefault(city, {})
    for phone in phones:
        result[city][phone] = name

print(result)