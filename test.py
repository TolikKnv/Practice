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

print('1 2 3 4'.split())