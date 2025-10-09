#3.1
# k=2
# l=4
# sp=[1,2,3,4,5,]
# sp=sp[:k-1]+sp[l:]
# print(sp)
# k=0
# for i in range(len(sp)):
#     k+=1
# print(sum(sp)/k)



#4.1
# import random
# l=[]
# a=0
# for i in range(0,20):
#     a=random.randint(1,50)
#     l+=[a]
# print(l)
# for i in range(len(l)):
#     if l[i]%2==0:
#         print(l[i])
# l=l[::-1]
# for i in range(len(l)):
#     if l[i]%2==1:
#         print(l[i])



#3.2
# import random
# l=[]
# a=0
# for i in range(0,20):
#     a=random.randint(-50,50)
#     l+=[a]
# print(l)
# kon=[l[i] for i in range(len(l)) if l[i]>0]
# kon.sort()
# print(kon[::-1])



#4.2
# import random
# l=[]
# a=0
# for i in range(0,20):
#     a=random.randint(-50,50)
#     l+=[a]
# print(l)
# el=[l[i] for i in range(len(l)) if abs(l[i])%2==0]
# print(el)
# el.sort()
# print(el)

#3.3
# import random
# m=5
# n=3
# board=[[1]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         board[i][j] = random.randint(-50, 50)
# print(*board,sep='\n')
#
# ma=-1000000000000
# mi=100000000000
# indma=0
# indmi=0
# for i in range(m):
#     for j in range(n):
#         if board[i][j]>ma:
#             ma=board[i][j]
#             indma=i
#         if board[i][j]<mi:
#             mi=board[i][j]
#             indmi=i
# board[indma],board[indmi]=board[indmi],board[indma]
# print()
# print(*board,sep='\n')

#4.3
# import random
# m=int(input('Введите m: '))
# n=int(input('Введите n: '))
# board=[[1]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         board[i][j] = random.randint(-50, 50)
# print(*board,sep='\n')
#
# mid=len(board)//2
# if len(board)%2==0:
#     for i in range(1,mid+1):
#         board[i-1],board[m-i]=board[m-i],board[i-1]
# if len(board)%2!=0:
#     for i in range(1,mid+1):
#         board[i-1],board[m-i]=board[m-i],board[i-1]
# print()
# print(*board,sep='\n')