# m = int(input())
# p = int(input())
# n = int(input())
# print(1,float(m))
# for i in range(n-1):
#     print(i + 2, m * (100 + p) / 100)
#     m = m * (100 + p) / 100

# q = int(input())
# w = int(input())
# d=q
# if q % 2 == 0:
#     d = q - 1
# for i in range((d - w) // 2 + 1):
#         print(d)
#         d = d - 2


# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
#         print(i)

# a = int(input())
# for i in range(1,11):
#     print(f'{a} x {i} = {a*i}')

# a = int(input())
# b = int(input())
# k = 0
# for i in range(a, b + 1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         k += 1
# print(k)

# n = int(input())
# k=0
# for _ in range(n):
#     k+=int(input())
# print(k)

# from math import *

# n = int(input())
# lg = log(n)
# s = 0
# for i in range(1, n + 1):
#     s += 1 / i
# print(s - lg)


# n = int(input())
# su = 0
# for i in range(1, n + 1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         su += i
# print(su)


# fac=1
# n = int(input())
# for i in range(1,n+1):
#     fac*=i
# print(fac)

# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         s += i
# print(s)

# flag=True
# for i in range(10):
#     a=int(input())
#     if a%2!=0:
#         flag=False
# if flag:
#     print('YES')
# else:
#     print('NO')


# n=int(input())
# ma1=-1000000000000000
# ma2=-10000000000000
# l=[]
# for i in range(n):
#     a=int(input())
#     l.append(a)
#     if a>ma1:
#         ma1=a
# for i in l:
#     if ma2<i<ma1:
#         ma2=i
# print(ma1,ma2,sep = '\n')


# n = int(input())
# if n > 1:
#     chi1 = 1
#     chi2 = 1
#     print(chi1, chi2, sep=" ", end=" ")
#     for i in range(n - 2):
#         print(chi1 + chi2, end=" ")
#         chi1, chi2 = chi2, chi1 + chi2
# else:
#     print("1")


# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2

# print(a)



i=0
while input()not in['стоп','хватит','достаточно']:
    i+=1
print(i)