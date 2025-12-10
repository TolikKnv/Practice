from datetime import *

# 7
# a
# s = input()
# a = lambda s, simbol: True if s[0]==simbol else False
# print(a(s,'a'))

# b
# l = ["sally", "Dylan", "rebecca", "Diana", "Joanne", "keith"]
# a = sum(map(lambda x: len(x) if x[0].isupper() else 0, l))
# print(a)


# v
# l = ["sally", "Dylan", "rebecca", "Diana", "Joanne", "keith"]
# q = input().split()
# a = list(filter(lambda x: x if x not in q else 0, l))
# print(a)


# 8
# a

# a = str(datetime.now())
# a = a.split()
# q = lambda x: [x[0].split('-')[0], x[0].split('-')[1], x[0].split('-')[2], x[1]]
# print(q(a))

# b
# l = [1,-1,3,-3,23,-2,33,-42,52]
# a = sum(filter(lambda x: x if isinstance(x,int) and x>0 else 0, l))
# b = sum(filter(lambda x: x if isinstance(x,int) and x<0 else 0, l))
# print(a,b,sep = '\n')

# v
# l = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

# d = lambda l: {i: sum(1 for x in l if x == i) for i in set(l)}
# print(d(l))


# res3 = lambda x: dict(zip(list(set(x)), list(map(lambda i: x.count(i), set(x)))))
# print(res3([3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]))


# try/except
# def func(s):
#     try:
#         return 2/s
#     except ZeroDivisionError:
#         return 'NO'
#     except TypeError:
#         return 'NO'

# print(func(0))

# assert!!!!!!!!!!!!!!!!!!
# def func(s):
#     try:
#         assert s!=0, 'нельзя делить на ноль'
#         assert type(s)!=str, 'нельзя строки'
#         return 2/s
#     except AssertionError as err:
#         return err
# print(func(0))

# raise
# def func(s):
#     try:
#         if s ==0:
#             raise ZeroDivisionError
#         elif type(s) == str:
#             raise TypeError
#         else:
#             return 2/s
#     except TypeError:
#         return 'нельзя строку'
#     except ZeroDivisionError:
#         return 'fuck your zero'
# print(func(0))

import math

# 6

# def func(a,b,c):
#     try:
#         d = b**2 - 4*a*c
#         return (b - math.sqrt(d))/(2*a), (b + math.sqrt(d))/(2*a)
#     except ZeroDivisionError:
#         return 'на ноль делить нельзя'
#     except ValueError:
#         return 'корней нет'
#     except TypeError:
#         return 'Введена буква'

# print(func('a',1,3))


# 1
# def validate_student_grades(grades: dict):
#     try:
#         assert all([isinstance(x, int) and not(1 <= x <= 100) for x in grades.values()]), False
#     except AssertionError as err:
#         return err
#     try:
#         if all([isinstance(x, str) for x in grades.keys()]):
#             return True
#     except TypeError:
#         return False

# print(validate_student_grades({"Alice": 'aad', "Bob": 100}))


# 2
# def safe_set_union(set1, set2):
#     try:
#         # set1 = set(set1)
#         # set2 = set(set2)
#         return set1|set2
#     except ValueError:
#         return 'Недопустимое значение'
#     except TypeError:
#         return 'Типы не соответсвуют'

# print(safe_set_union({2:34}, 'asdfg') )


# 3
# def get_nested_value(data: dict, keys: list):
#     try:
#         assert keys != [], 'Список пуст'
#     except AssertionError as err:
#         return err
#     try:
#         s = data[keys[0]]
#         for i in keys[1:]:
#             s = s[i]
#         return s
#     except KeyError:
#         return 'KeyError'

# data = {"user": {"profile": {"name": {'q':'qwe'}}}}
# print(get_nested_value(data, ["user", "profile", "name",'q']))


# 4
# def validate_email_set(emails: set):
#     try:
#         if all([isinstance(i,str) for i in emails]) and all(['@' in i for i in emails]):
#             return 'Все email валидны'
#         else:
#             raise ValueError
#     except ValueError:
#         return 'Какой то email не валиден'

# a = {'qwer@123', 123,'qq3ds@123'}
# print(validate_email_set(a))


# 5
# def merge_dicts_safe(dict1: dict, dict2: dict):
#     try:
#         assert isinstance(dict1, dict), "словарь 1 не словарь"
#         assert isinstance(dict2, dict), "словарь 1 не словарь"
#         for i in dict1.keys():
#             for j in dict2.keys():
#                 if j == i:
#                     raise KeyError
#         for k, v in dict2.items():
#             dict1.update({k: v})
#         print(dict1)
#     except KeyError:
#         a = []
#         for i in dict1.keys():
#             for j in dict2.keys():
#                 if j == i:
#                     a.append(j)
#         print(f"Ключи {a} совподают")
#     except AssertionError as err:
#         print(err)


# merge_dicts_safe({"a": 1}, {"b": 2})
# merge_dicts_safe({"a": 1}, 6)



