# import math
# a=2
# x=float(input())
# y=(x**2/a)+math.cos(2*x-1)
# print(y)

# import numpy as np
# import math
# import matplotlib.pyplot as plt

# a = 2
# x = np.arange(-10, 10, 0.1)
# y = (x**2 / a) + math.cos(2 * x)
# e = math.cos(2 * x)
# fig = plt.subplots()
# plt.plot(x, y, linewidth=2)
# plt.plot(x, y, linewidth=4)
# plt.grid()
# plt.show()

import matplotlib.pyplot as plt
import math

x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
print(type(x))
y = []
y1 = []
a = 2
for i in x:
    y.append((i**2 / a) + math.cos(2 * i - 1))
for j in x:
    y1.append(j)
q = -4
step = 0.1
while q < 4:
    if round((q**2 / a) + math.cos(2 * q - 1), 1) == round(q, 1):
        print(f"x={q}   y={q}")
    # print(round(x0,1))
    q = q + step
print(x)
print(y)
print(y1)
plt.plot(x, y, "g*-")
plt.plot(x, y1, "r*-")
plt.show()

# str='Иванов Иван Иванович'
# str=str.split()
# print('|{:10}|{:10}|'.format('Фамилия',str[0]))
# print('|{:10}|{:10}|'.format('Имя',str[1]))
# print('|{:10}|{:10}|'.format('Отчество',str[2]))
# print(f'|{'Фамилия':10}|{str[0]:10}|')
# print(f'|{'Имя':10}|{str[0]:10}|')
# print(f'|{'Отчество':10}|{str[0]:10}|')
# print()

# a=int(input())
# print(f"""
# Цифра в позиции тысяч равна {a//1000}
# Цифра в позиции сотен равна {a//100%10}
# Цифра в позиции десятков равна {a//10%10}
# Цифра в позиции единиц равна {a%10}
#       """)

# n=str(input())
# print(int(n)+int(n+n)+int(n+n+n))
