# import matplotlib.pyplot as plt
# import math
# from scipy.optimize import fsolve
#
# x=[-4,-3,-2,-1,0,1,2,3,4]
# y=[]
# y1=[]
# a=2
# for i in x:
#     y.append((i**2/a)+math.cos(2*i-1))
# for j in x:
#     y1.append(j)
#
# # функция разности
# def func(x):
#     return (x**2/a + math.cos(2*x-1)) - x
#
# # поиск пересечений (берем разные стартовые точки)
# roots = []
# for guess in range(-4, 5):
#     root = fsolve(func, guess)[0]
#     # округлим, чтобы избежать дублей
#     root = round(root, 6)
#     if root not in roots:
#         roots.append(root)
#
# print("Точки пересечения:")
# for r in roots:
#     print(f"x = {r}, y = {round(r,6)}")
#
# # графики
# plt.plot(x,y,'g*-',label='y = x^2/2 + cos(2x-1)')
# plt.plot(x,y1,'r*-',label='y = x')
# plt.legend()
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import math
# x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
# x1=[-5,-4,-3,-2,-1]
# x2=[1,2,3,4,5]
# x3=[]
# y=[]
# y1=[]
# y2=[]
# y3=[]
# y4=[]
# y5=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
# k1=2
# k2=-2
# for i in x1:
#     y.append(k1/i)
# for i in x2:
#     y1.append(k1/i)
# for j in x1:
#     y2.append(k2/j)
# for i in x2:
#     y3.append(k2/i)
# for j in x:
#     y4.append(0)
# for j in y5:
#     x3.append(0)
# print(x)
# print(y)
# print(y1)
# plt.plot(x1,y,'g*-')
# plt.plot(x1,y2,'y*-')
# plt.plot(x2,y1,'r*-')
# plt.plot(x2,y3,'y*-')
# plt.plot(x,y4,'b*-')
# plt.plot(x3,y5,'b*-')
# plt.show()

# import matplotlib.pyplot as plt
# import math
# x0=[-2,-1,0,1,2]
# x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
# x1=[-5,-4,-3,-2,-1]
# x2=[1,2,3,4,5]
# x3=[]
# y=[]
# y1=[]
# y2=[]
# y4=[]
# y5=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
# k1=2
# k2=-2
# for i in x0:
#     y.append(-i**2)
# for i in x2:
#     y1.append(k1/i)
# for j in x1:
#     y2.append(k2/j)
# for j in x:
#     y4.append(0)
# for j in y5:
#     x3.append(0)
# print(x)
# print(y)
# print(y1)
# plt.plot(x1,y2,'y*-')
# plt.plot(x2,y1,'r*-')
# plt.plot(x0,y,'g*-')
# plt.plot(x,y4,'b*-')
# plt.plot(x3,y5,'b*-')
# plt.show()
print('egref')
def sum_list(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    print(sum)
list=[1,3,5,234,2,5,2]
sum_list(list)