from math import *

# l1 = ['1', '123', '123', '12', '1', '123']
# l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
# d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
# d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}


# 5
# l2 = [i+1 if l2[i]<0 else l2[i] for i in range(len(l2))]
# print(l2)

# 7
# s = [1,2,'a',3,4,'b','c','d','e']
# s2 = [i for i in s if str(i).isalpha()]
# s1 = [i for i in s if str(i).isdigit()][::-1]+[0]*len(s2)
# d = dict(zip(s2,s1))
# print(s1,s2,d)


# 8
# s = "Маша гуляет, Коля работает, дома Ваня, закупается Женя"
# s1 = s.split(", ")
# s1 = [(i.split()[0], i.split()[1]) if i[0].isupper() == True else (i.split()[1], i.split()[0]) for i in s1]
# s1.sort()
# print(dict(s1))


#9
# s = 'Имеется предложение, слова в котором, разделяются пробелами. С помощью генератора списков получить слово, состоящее из первых букв слов в предложении'
# l = [i[0].lower() for i in s.split()]
# print(''.join(l).capitalize())

#10
# ln = []


# def prod(x:float,y:float) -> float:
#     '''
#     Возвращает произведение двух чисел

#     Парметры:
#     x (Float): первый множитель
#     y (Float): второй множитель

#     Возвращает:
#     float: Произведение

#     '''

#     return x*y

# print(prod(2,4))
# print(prod.__doc__)

#1
# a = map(int,input().split())
# print(sum(a))

#2
# with open("input.txt", "r") as f:
#     a, b = map(int, f.read().split())

# with open("output.txt", "w") as f:
#     f.write(str(a + b))