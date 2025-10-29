# 4
# s = [
#     "января",
#     "февраль",
#     "март",
#     "апрель",
#     "май",
#     "июнь",
#     "июль",
#     "август",
#     "сентябрь",
#     "октябрь",
#     "ноябрь",
#     "декабрь",
# ]
# d = {}

# for i in range(0, 12):
#     d[s[i]] = i + 1
# print(d)

# date = "1 января 2021"
# date = date.split()
# output = []
# output += [date[0]]
# if d[date[1]] < 10:
#     output += ["0" + str(d[date[1]])]
# else:
#     output += [d[date[1]]]
# output += [date[2]]
# print(output, sep=".")


# 8
# s = 'ten,one,five,two,three,four'
# s= s.split(',')
# d={}
# for i in range(len(s)):
#     d[s[i]]=f'номер {i+1} в строке'
# print(d)


# 7
# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# chars = ["-.", ".-", "..", ".-.", "..-", "--.", ".--", ".-.-", "-.-.", "..--"]
# d = {}
# for i in range(len(letters)):
#     d[chars[i]] = letters[i]

# a = input()
# words=[]
# words = a.split('   ')
# morze = []
# for i in words:
#     i = i.split(' ')
#     morze.append(i)
#     print(i)

# for i in morze:
#     for j in range(len(i)):
#         i[j]=d[i[j]]

# for i in range(len(morze)):
#     morze[i]=''.join(morze[i])

# print(*morze,sep = ' ')


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
p_l = phones_list.copy()
for i in range(len(phones_list)-1):
    for j in range(i+1, len(phones_list)):
        if phones_list[i]['name']==phones_list[j]['name'] and phones_list[i]['city']==phones_list[j]['city']:
            for q in phones_list[j]['phones']:
                if q in phones_list[i]['phones']:
                    continue
                else:
                    phones_list[i]['phones'].append(q)
                    p_l[i]['phones'].append(q)
            p_l.pop(i)

print(*phones_list,sep = '\n')
print()
print(*p_l,sep = '\n')
