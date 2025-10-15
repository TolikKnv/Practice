# # объявление функции
# def print_fio(name, surname, patronymic):
#     s=surname[0].upper()+name[0].upper()+patronymic[0].upper()
#     s.upper()
#     print(s)
# # считываем данные
# name, surname, patronymic = input(), input(), input()

# # вызываем функцию
# print_fio(name, surname, patronymic)



# объявление функции
# def print_case_counts(s):
    # U,L=0,0
    # q=[]
    # q.extend(s)
    # for i in q:
    #     if i.isalpha() and i==i.upper():
    #         U+=1
    #     elif i.isalpha() and i==i.lower():
    #         L+=1
    # print(f'Букв в верхнем регистре: {U}')
    # print(f'Букв в нижнем регистре: {L}')

# # считываем данные
# s = input()

# # вызываем функцию
# print_case_counts(s)



# # объявление функции
# def print_digit_sum(num):
#     su=0
#     while num>0:
#         su+=num%10
#         num=num//10
#     print(su)

# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)




# # объявление функции
# def print_sorted_hyphen(s):
#     l=s.split('-')
#     l.sort()
#     print(*l,sep='-')

# # считываем данные
# s = input()

# # вызываем функцию
# print_sorted_hyphen(s)



# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(1,base//2+2):
#         print(fill*i)
#     for i in range(base//2,0,-1):
#         print(fill*i)

# # считываем данные
# fill = input()
# base = int(input())

# # вызываем функцию
# draw_triangle(fill, base)




# объявление функции
# def print_perm_time_call(msc_time):
#     perm_hour=int(msc_time[:2])+2
#     if perm_hour<10:
#         print('Созвон будет в '+'0'+str(perm_hour)+msc_time[2:]+'.')
#     else:
#         print('Созвон будет в '+str(perm_hour)+msc_time[2:]+'.')

# # считываем данные
# msc_time = input()

# # вызываем функцию
# print_perm_time_call(msc_time)



# объявление функции
def print_symbol_counts(s):
    l=[]
    l.extend(s.lower())
    l.sort()
    k=0
    for i in range(len(l)):
        if l[i]!=l[i-1]:
            for j in l:
                if l[i]==j:
                    k+=1
            print(f'{l[i]}: {k}')
            k=0

# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)