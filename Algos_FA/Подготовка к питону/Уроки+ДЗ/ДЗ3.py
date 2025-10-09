import math
a=float(input('Введите а: '))
b=float(input('Введите b: '))
step=0.1
k=a
while k<=b:
    print(f'|{k:^8.2f}|{math.sin(k):^8.2f}|')
    k+=step