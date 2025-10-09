#1

# import random
# from operator import truediv
#
# l=[0,0,0]
# while sum(l)!=1:
#     for i in range(0,len(l)):
#         l[i]=random.randint(0,1)
# print(l)
#
#
#2
# nach = False
# while nach!=True:
#     door = int(input('Выберите дверь от 1 до 3: '))
#     if l[door-1]==1:
#         print('Вы нашли приведение')
#         nach = True
#     else:
#         print('За этой дверью нет приведения')
#         nach = False

# import random
#
# seven = 7
#
# znach = 0
#
# do='next'
#
# while do!='stop':
#     znach = random.randint(-30,30)
#     print(f'Чему равно 7 * {znach}: ', end='')
#     otv = int(input())
#     if otv == seven*znach:
#         print('Вы правы')
#     else:
#         print(f'Не правильно. Правильный ответ = {znach*seven}')
#
#     do = input('Введите "stop" или "next": ')


#3
# import random
#
# podl = ["Лягушка-философ", "Динозавр-вегетарианец", "Кофе, который устал бодрить", "Сыр с комплексом неполноценности", "Метла-интроверт", "Кот-конспиролог", "Кактус-романтик", "Танцующий холодильник", "Телефон, уставший от уведомлений", "Одинокий носок, ищущий пару"]
# skaz = ["танцует в библиотеке", "пишет мемуары по ночам", "боится понедельников", "учится играть на гитаре", "спорит с телевизором", "мечтает о тостере", "забывает, зачем пришёл", "поёт в душе на латыни", "планирует мировое господство", "притворяется Wi-Fi роутером"]
# vtor = ["в розовых тапочках", "под дождём из попкорна", "на крыше старого автобуса", "с чашкой холодного чая", "в обществе скучающих пингвинов", "под звуки баяна", "среди забытых носков", "в магазине мечтаний", "на диване философских размышлений", "в поисках потерянного вайфая"]
#
# pred = ''
# pred+= random.choice(podl)
# pred+= random.choice(skaz)
# pred+= random.choice(vtor)
#
# print(pred)


#4
# import random
#
# a=[random.randint(1,99) for i in range(2)]
# b=[random.randint(1,99) for i in range(2)]
#
# sp1str = str(a[0])+'.'+str(a[1])
# sp2str = str(b[0])+'.'+str(b[1])
#
#
# cp1 = float(sp1str)
# cp2 = float(sp2str)
# print(cp1,cp2,sep='\n')
#
#
#
# print(f'Сумма = {cp1+cp2}')
# print(f'Разность = {abs(cp1-cp2)}')



#5
# import random
# l=[]
# for i in range(100):
#     l.append(random.randint(2,5))
#
# q = l
#
# print(l)
# l.sort()
# print(l)
#
# for i in range(0,len(q)):
#     for j in range(0,len(q)):
#         if q[j]>q[i]:
#             q[j],q[i]=q[i],q[j]
# print(q)