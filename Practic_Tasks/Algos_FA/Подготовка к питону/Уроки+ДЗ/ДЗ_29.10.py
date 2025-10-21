from random import *

# n=5
# m=6
# matrix = []
# for i in range(n):
#     s=[]
#     for j in range(m):
#         s.append(random.randint(-5,5))
#     matrix.append(s)
# print(*matrix,sep='\n')
# print()
# del_matrix,extended_matrix = matrix,matrix
# # number 1
# k=0
# for i in matrix:
#     for j in i:
#         if j==0:
#             k+=1
#             break
# print(k)
# print()

# number 2
# for i in matrix:
#     k=0
#     for j in matrix:
#         if i==j:
#             k+=1
#     if k>=2:
#         print('YES')
#         k=0
#         break
# if k==1:
#     print('NO')
# print()


# number 3
"""
Транспонирование матрицы
"""
# transposed_matrix=[]
# for i in range(len(matrix[0])):
#     j1=[]
#     for j in matrix:
#         j1.append(j[i])
#     transposed_matrix.append(j1)
# print(*transposed_matrix,sep='\n')


# number 4
# col = int(input('Введите номер столбца: '))
# str = int(input('Введите номер строки: '))
# del del_matrix[str-1]
# for i in del_matrix:
#     del i[col-1]
# print(*del_matrix,sep='\n')


# number 5
# l=[0]*(m+1)
# col1 = int(input('Введите номер столбца: '))
# str1 = int(input('Введите номер строки: '))
# for i in extended_matrix:
#     i.insert(col1-1,0)
# extended_matrix.insert(str1-1,l)
# print(*extended_matrix,sep='\n')

# Умножение матриц
# def tr(a, n, m):
#     s = [[0 for _ in range(n)] for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             s[j][i] = a[i][j]
#     return s

# print('NxM and MxK')
# n = int(input())
# m = int(input())
# k = int(input())

# s = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
# print(*s, sep='\n')
# print()
# s2 = [[random.randint(-10, 10) for _ in range(k)] for _ in range(m)]
# print(*s2, sep='\n')
# print()

# ans = [[0 for _ in range(k)] for _ in range(n)]

# s2 = tr(s2, m, k)

# for i in range(n):
#     for j in range(k):
#         t = 0
#         for x in range(m):
#             t += s[i][x]*s2[j][x]
#         ans[i][j] = t
# print(*ans, sep='\n')


# №1 со страницы 50

# tuple = set()
# for i in range(10):
#     tuple.add(randint(1, 100))
# print(tuple)
# d = []
# for i in range(len(tuple)):
#     d.append(i)
# print(dict(zip(d, tuple)))


# №2 со страницы 50
# mixed_tuple = ("Alice", 25, 3.14, True, [1, 2, 3], {"city": "London"})
# print(mixed_tuple)

# people = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
# names, ages = zip(*people)
# names = list(names)
# ages = list(ages)

# print(names)
# print(ages)`


# №3 со страницы 50

# tuple = {1,2,3,4,5,6,7,8,9,10}
# print(next(iter(tuple)))
# l_tuple = list(tuple)
# print(l_tuple[::-1])




# №4 со страницы 50

# tuple = (1,2,3)
# num1,num2,num3 = tuple
# print(num1,num2,num3)
# d_tuple = (('name','Bob'),('age',12),('city','New York'))
# dict_tuple = dict(d_tuple)
# print(dict_tuple)


# №5 со страницы 50

# tuple = (100,200)
# tuple = tuple + (300,)
# print(f'это кортеж {tuple}')