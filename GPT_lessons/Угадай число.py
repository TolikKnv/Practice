import random
n=random.randint(1,100)
print('Я загадал число от 1 до 100, попробуй угадать!!!')
z=int(input('Введи число:'))
while z != n:
    if z>n:
        print('Моё число меньше')
        z = int(input('Введи число:'))
    elif z<n:
        print('Моё число больше')
        z = int(input('Введи число:'))
print(f'Ты угадал, число = {z}')