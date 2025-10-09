# l=[]
# for i in range(1,26+1):
#     l+=[chr(96+i)*i]
# print(l)

# n=int(input())
# l=[]
# for i in range(n):
#     num=int(input())
#     l.append(num**3)
# print(l)

# n = int(input())
# l=[]
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# print(l)

# n=int(input())
# l=[]
# s=int(input())
# for i in range(n-1):
#     s1=int(input())
#     l.append(s1+s)
#     s=s1
# print(l)

# n=int(input())
# l=[]
# for i in range(0,n):
#     s=int(input())
#     l.append(s)
# for i in range(1,len(l)//2+1):
#     del l[i]
# print(l)

# n=int(input())
# l=[]
# for i in range(n):
#     s=input()
#     l+=[s]
# k=int(input())
# s=''
# for i in range(len(l)):
#     if len(l[i])>=k:
#         s+=l[i][k-1]
# print(s)

n=int(input())
l=[]
for i in range(n):
    s=input()
    l.extend(s)
print(l)