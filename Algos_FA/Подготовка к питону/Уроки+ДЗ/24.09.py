# print('_______________________')
# print('|{:^10}|{:^10}|'.format('Студент','Оценка'))
# list=('Иванов','Петров','Сидоров')
# list2=(3,4,5)
# print('|{:^10}|{:^10}|'.format(list[0],list2[0]))
# print('|{:^10}|{:^10}|'.format(list[1],list2[1]))
# print('|{:^10}|{:^10}|'.format(list[2],list2[2]))


# s=input('Введите слова:')
# let=input('Введите букву:')
# k=0
# for i in range(len(s)):
#     if s[i]==let:
#         k+=1
# print(k)

# s=input('Введите слова:')
# let=input('Введите букву:')
# s=s.split()
# word=''
# maximum=0
# k=0
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         if s[i][j]==let:
#             k+=1
#     if k/len(s[i])*100>maximum:
#         maximum=k/len(s[i])*100
#         word=s[i]
#         k=0
# print(word,maximum)

# import matplotlib.pyplot as plt
# import math
# x=-math.pi/2
# y1=[]
# y2=[]
# y3=[]
# x1=[]
# x2=[]
# x3=[]
# while x<=2*math.pi:
#     if x>4.5:
#         y=3*x**2
#         x1.append(x)
#         y1.append(y)
#     if 1<=x<=4.5:
#         y=math.exp(-x)
#         x2.append(x)
#         y2.append(y)
#     if x<1:
#         y=-(math.cos(2*x))**2
#         x3.append(x)
#         y3.append(y)
#     x+=0.1
# plt.plot(x1, y1, 'g*-')
# plt.plot(x2, y2, 'r*-')
# plt.plot(x3, y3, 'y*-')
# plt.title('Задание 20')
# plt.xlabel('ось x')
# plt.ylabel('ось y')
# plt.legend(['F(x1)=3*x**2', 'F(x2)=math.exp(-x2)', 'F(x3)=math.exp(-x3)'])
# plt.show()


# ma=-1000000000000000000000
# mi=10000000000000000000000
# sum=0
# k=0
# while True:
#     x=int(input())
#     if x==0:
#         break
#     sum = sum + x
#     k += 1
#     if x > ma:
#         ma = x
#     if x < mi:
#         mi = x
# print(mi,ma,sum/k)


# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

