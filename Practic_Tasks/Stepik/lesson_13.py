from math import *



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
# def print_symbol_counts(s):
#     l=[]
#     l.extend(s.lower())
#     l.sort()
#     k=0
#     for i in range(len(l)):
#         if l[i]!=l[i-1]:
#             for j in l:
#                 if l[i]==j:
#                     k+=1
#             print(f'{l[i]}: {k}')
#             k=0

# # считываем данные
# s = input()

# # вызываем функцию
# print_symbol_counts(s)


# # объявление функции
# def code_format(text):
#     return f'<code>{text}</code>'

# # считываем данные
# text = input()

# # вызываем функцию
# print(code_format(text))


# # объявление функции
# def get_days(month):
#     if month in range(1,8,2) or month in range(8,13,2):
#         return 31
#     if month==2:
#         return 28
#     if month in range(4,7,2) or month in range(9,12,2):
#         return 30

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))


# # объявление функции
# def math_round_to_int(num):
#     if num % 1 >= 0.5:
#         return int(num) + 1
#     else:
#         return int(num)

# # считываем данные
# num = float(input())

# # вызываем функцию
# print(math_round_to_int(num))


# объявление функции
# def get_factors(num):
#     l=[]
#     for i in range(1,num+1):
#         if num%i==0:
#             l.append(i)
#     return(l)
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))


# # объявление функции
# def number_of_factors(num):
#     l=0
#     for i in range(1,num+1):
#         if num%i==0:
#             l+=1
#     return(l)

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_of_factors(n))


# # объявление функции
# def get_unique(numbers):
#     l=[]
#     for i in numbers:
#         if i in l:
#             continue
#         else:
#             l.append(i)
#     return l
# # считываем данные
# numbers = eval(input())

# # вызываем функцию
# print(get_unique(numbers))


# объявление функции
# def get_last_index(data, value):
#     ind=0
#     for i in range(len(data)):
#         if value==data[i]:
#             ind=i
#     if value not in data:
#         print('ERROR!')
#         exit()
#     return ind

# # считываем данные
# data = eval(input())
# value = eval(input())

# # вызываем функцию
# print(get_last_index(data, value))


# объявление функции
# def find_all(target, symbol):
#     l=[]
#     if symbol not in target:
#         l=[]
#         return l
#         exit()
#     else:
#         for i in range(len(target)):
#             if target[i]==symbol:
#                 l.append(i)
#     return l
# # считываем данные
# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))


# объявление функции
# def merge(list1, list2):
#     l=list1+list2
#     l.sort()
#     return l

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))


# def quick_merge(list1, list2):
#     result = []

#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2

#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1

#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     else:  # иначе прицепляем остаток другого списка
#         result += list2[p2:]

#     return result


# def total(kol):
#     l1 = input().split()
#     l1=[int(j) for j in l1]
#     l2 = input().split()
#     l2=[int(j) for j in l2]
#     total_list = quick_merge(l1, l2)
#     for i in range(kol - 2):
#         l4 = input().split()
#         l4=[int(j) for j in l4]
#         total_list = quick_merge(total_list, l4)
#     return total_list


# n = int(input())
# print(*total(n))




# объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
#         return True
#     else:
#         return False

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))



# объявление функции
# def is_palindrome(text):
#     text = text.lower()
#     text="".join(c for c in text if c.isalpha())
#     if text==text[::-1]:
#         return True
#     else:
#         return False

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_palindrome(txt))




# # объявление функции
# def is_one_away(word1, word2):
#     k=0
#     if len(word1)==len(word2):
#         for i in range(len(word1)):
#             if word1[i]!=word2[i]:
#                 k+=1
#         if k==1:
#             return True
#         else:
#             return False
#     else:
#         return False

# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))



# # объявление функции
# def convert_to_python_case(text):
#     result = text[0].lower()
#     for chr in text:
#         if chr.isupper():
#             result += '_' + chr.lower()
#         else:
#             result += chr
#     return result

# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))




# # объявление функции
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#         else:
#             continue
#     return True

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))




# объявление функции
# def get_next_prime(num):
#     for i in range(num+1, num*1000):
#         if is_prime(i):
#             return i
#         exit()

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))





# # объявление функции
# def is_password_good(password):
#     k1,k2,k3=0,0,0
#     if len(password)>=8:
#         for chr in password:
#             if chr in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#                 k1+=1
#             if chr in 'qwertyuiopasdfghjklzxcbnm':
#                 k2+=1
#             if chr in '1234567890':
#                 k3+=1
#     if k1>0 and k2>0 and k3>0 and len(password)>=8:
#         return True
#     else:
#         return False

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))




# # объявление функции
# def is_correct_bracket(text):
#     if text.count('(')!=text.count(')'):
#         return False
#     else:
#         k=0
#         for chr in text:
#             if chr=='(':
#                 k+=1
#             if chr==')':
#                 k-=1
#             if k<0:
#                 return False
#         return True


# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))





# объявление функции
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#         else:
#             continue
#     return True

# # объявление функции
# def is_valid_password(password):
#     l=password.split(':')
#     if len(l)!=3:
#         return False
#     if l[0]==l[0][::-1] and is_prime(int(l[1])) and int(l[2])%2==0:
#         return True
#     else:
#         return False

# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))



# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     return (x1+x2)/2, (y1+y2)/2

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)




# # объявление функции
# def get_circle(radius):
#     return 2*pi*radius, pi*radius**2

# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)




# объявление функции
def solve(a, b, c):
    disc = b**2 - 4 * a * c
    if disc < 0:
        print("Нет корней")
    elif disc == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        lum = []
        lum += [(-b + sqrt(disc)) / (2 * a)]
        lum += [(-b - sqrt(disc)) / (2 * a)]
        lum.sort()
        return lum[0],lum[1]

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)