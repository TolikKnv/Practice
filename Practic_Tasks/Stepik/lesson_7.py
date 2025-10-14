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


# i=0
# while input()not in['стоп','хватит','достаточно']:
#     i+=1
# print(i)


# n = int(input())
# while n%7==0:
#     print(n)
#     n = int(input())

# n = int(input())
# sum=0
# while n>0:
#     sum+=n
#     n = int(input())
# print(sum)

# n = int(input())
# k=0
# while not(n<0 or n>5):
#     if n==5:
#         k+=1
#     n = int(input())
# print(k)


# n = int(input())
# k=0
# while n//25>0:
#     k+=1
#     n-=25
# while n//10>0:
#     k+=1
#     n-=10
# while n//5>0:
#     k+=1
#     n-=5
# while n//1>0:
#     k+=1
#     n-=1
# print(k)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10

# print(product)

# n = int(input())
# v= n
# sum = 0
# kol = 0
# product = 1
# av = 0
# num1 = 0
# num1_num_last = 0
# while n>0:
#     sum+=n%10
#     kol+=1
#     product*=n%10
#     n = n//10
# av=sum/kol
# num1=v//(10**(kol-1))
# num1_num_last= num1+v%10
# print(sum,kol,product,av,num1,num1_num_last,sep='\n')


# n= int(input())
# l=[]
# otv = 'YES'
# chi = n%10
# n=n//10
# while otv == 'YES' and n>0:
#     if n%10==chi:
#         otv = 'YES'
#         n=n//10
#     else:
#         otv = 'NO'
# print(otv)

# n = int(input())
# k=0
# v=n
# while n>0:
#     k+=1
#     n=n//10
# print((v//(10**(k-2)))%10)


# n = int(input())
# otv = "YES"
# while n > 9:
#     if n % 10 <= n // 10 % 10:
#         otv = "YES"
#         n = n // 10
#     else:
#         otv = "NO"
#         break
# print(otv)


# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')


# n=int(input())
# for i in range(2,100000):
#     if n%i==0:
#         print(i)
#         break


# n=int(input())
# for i in range(1,n+1):
#     if (i in range(5,10)) or (i in range(17,38)) or (i in range(78,88)):
#         continue
#     else:
#         print(i)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# n = int(input())
# for i in range(1,n+1):
#     for j in range(5):
#         print(i,end=' ')
#     print()


# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,10):
#         print(f'{i} + {j} = {i+j}',end=' ')
#     print()


# n = int(input())
# for i in range(1):
#     for j in range(1,n//2+2):
#         print('*'*j,end='\n')
#     for j in range(n//2,0,-1):
#         print('*'*j,end='\n')


# n=int(input())
# for j in range(1,n+1):
#     print(str(j)*j,end='\n')


# for n in range(100):
#     for k in range(100):
#         for m in range(100):
#             if 0.5*k+5*m+10*n==100 and n+k+m==100:
#                 print(n,m,k)


# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d,151):
#                     if (int(1/5)*(int(a**5)+int(b**5)+int(c**5)+int(d**5)))==e:
#                         print(a+b+c+d+((int(1/5)*(int(a**5)+int(b**5)+int(c**5)+int(d**5)))))
#                         break

# n = int(input())
# z=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(z,end=' ')
#         z+=1
#     print()

# n = int(input())
# for i in range(1,n+1):
#     s=[]
#     for j in range(1,i+1):
#         s+=[j]
#     print(*s,sep='',end='')
#     s.pop()
#     s.reverse()
#     print(*s,sep='')


# n=int(input())
# for i in range(1,n+1):
#     print(i,end='')
#     for j in range(1,n+1):
#         if i%j==0:
#             print('+',end='')
#     print()


# a=int(input())
# b=int(input())
# ma=-111111111111
# ma_num=0
# for i in range(a,b+1):
#     k=0
#     for j in range(1,i+1):
#         if i%j==0:
#             k+=j
#         if k>=ma:
#             ma=k
#             ma_num=i
# print(ma_num,ma)


# n = input()
# l=[]
# l.extend(n)
# sum=1000000
# su=0
# while sum>9:
#     for i in l:
#         su+=int(i)
#     sum=su
#     l=[]
#     l.extend(str(sum))
#     su=0
# print(sum)


# su=0
# n = int(input())
# for i in range(1,n+1):
#     fac=1
#     for i in range(1,i+1):
#         fac*=i
#     su+=fac
# print(su)


# a,b=int(input()),int(input())
# k=0
# for i in range(a,b+1):
#     for j in range(2,i):
#         if i%j==0:
#             k+=1
#             break
#     if k==0:
#         print(i)
#     else:
#         k=0



