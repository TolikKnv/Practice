# a = int(input())
# b = int(input())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print((a**10+b**10)**0.5)


# weight = float(input())
# high = float(input())
# imt = weight / high**2
# if imt < 18.5:
#     print("Недостаточная масса")
# elif imt > 25:
#     print("Избыточная масса")
# else:
#     print("Оптимальная масса")


# s = input()
# dl = len(s) * 60
# print(f"{dl//100} р. {dl%100} коп.")


# s = input()
# words = s.split()
# print(len(words))


# year = int(input())
# l = [
#     "Обезьяна",
#     "Петух",
#     "Собака",
#     "Свинья",
#     "Крыса",
#     "Бык",
#     "Тигр",
#     "Заяц",
#     "Дракон",
#     "Змея",
#     "Лошадь",
#     "Овца",
# ]
# print(l[year % 12])


# num = input()
# if len(num) == 5:
#     print(int(num[::-1]))
# else:
#     print(int(num[0] + num[-5:][::-1]))


# num = input()
# l = []
# l.extend(num)
# ind = len(l) + len(l) // 3 - 1
# if len(l) % 3 == 0:
#     for i in range(3, ind, 4):
#         l.insert(i, ",")
# elif len(l) % 3 == 1:
#     for i in range(1, ind, 4):
#         l.insert(i, ",")
# elif len(l) % 3 == 2:
#     for i in range(2, ind, 4):
#         l.insert(i, ",")
# l = "".join(l)
# print(l)



# n = int(input())
# col1 = 0
# col2 = 0
# col3 = 0
# col4 = 0
# for i in range(n):
#     coord = input().split()
#     if int(coord[0])>0 and int(coord[1])>0:
#         col1 += 1
#     if int(coord[0])<0 and int(coord[1])>0:
#         col2 += 1
#     if int(coord[0])<0 and int(coord[1])<0:
#         col3 += 1
#     if int(coord[0])>0 and int(coord[1])<0:
#         col4 += 1
# print(f'''
# Первая четверть: {col1}
# Вторая четверть: {col2}
# Третья четверть: {col3}
# Четвертая четверть: {col4}''')



nums = input().split()
nums = [int(i) for i in nums]
k = 0
for i in range(1,len(nums)):
    if nums[i-1]<nums[i]:
        k+=1
print(k)




