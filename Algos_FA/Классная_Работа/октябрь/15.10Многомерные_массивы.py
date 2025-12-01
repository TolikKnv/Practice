import random

n=5
m=6
matric = []
for i in range(n):
    str=[]
    for j in range(m):
        str.append(random.randint(-5,5))
    matric.append(str)
print(*matric,sep='\n')
print()
# number 1
k=0
for i in matric:
    for j in i:
        if j==0:
            k+=1
            break
print(k)
print()

# number 2
for i in matric:
    k=0
    for j in matric:
        if i==j:
            k+=1
    if k>=2:
        print('YES')
        k=0
        break
if k==1:
    print('NO')
print()



# number 3
'''
Транспонирование матрицы
'''
# trancp_matric=[]
# for i in range(len(matric[0])):
#     j1=[]
#     for j in matric:
#         j1.append(j[i])
#     trancp_matric.append(j1)
# print(*trancp_matric,sep='\n')


# number 4
