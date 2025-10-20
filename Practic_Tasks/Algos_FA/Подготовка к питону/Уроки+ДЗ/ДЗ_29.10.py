# import random

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
'''
Транспонирование матрицы
'''
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



#number 5
# l=[0]*(m+1)
# col1 = int(input('Введите номер столбца: '))
# str1 = int(input('Введите номер строки: '))
# for i in extended_matrix:
#     i.insert(col1-1,0)
# extended_matrix.insert(str1-1,l)
# print(*extended_matrix,sep='\n')

# Умножение
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
