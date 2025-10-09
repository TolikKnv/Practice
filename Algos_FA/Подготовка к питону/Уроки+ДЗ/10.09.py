# print('Введите число из 2 цифр')
# a=int(input())
# print(str(a), a, float(a),sep=',')
# print()
# print(str(a))
# print(a)
# print(float(a))
from operator import index

# a='Компьютерный практикум'
# print(a[0:4])
# print(a[-22:-18])
# print(a.split('ь')[0])

# a='Компьютерный практикум'
# print(a[1::2])

# s='gfhnf'
# c=len(s)//2
# if len(s)%2 == 0:
#     print(s[c-c//2:c+c//2])
# else:
#     print(s[c-c // 2:c + c // 2+1])

# s='one'*6+'two'*3
# print(s)

# a=input()
# print(a)
# print(a[1])
# print(a[-2])
# print(a[:3])
# print(a[:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))

# s = input()
# first = s.find('*')
# last = s.rfind('*')
# #print(first,last)
# if first == -1:
#     print('нет символа')
# elif first == last:
#     print(first)
# else:
#     s_2 = s.find('*', first + 1)
#     print(first,s_2,last)
# new_s = s.replace('*', '', 1)
# new_s = new_s[::-1].replace('*', '', 1)[::-1]
# print(new_s)

# s=input()
# d=' '
# q=s.split(' ')
# print(d.join(q))
# print(q.strip)

# print('name=',end='')
# name=input()
# print('age=',end='')
# age=input()
# print(f'Hello, {name}! Your age is {age}')

# import random
# a=random.randint(1,10)
# b=int(input())
# while b!=a:
#     if a<b:
#         print('a<b')
#     elif a>b:
#         print('a>b')
#     b=int(input())
# print('that`s right')

# list=[1,2,3,4,5]
# print(list[0],list[4])
# list[2]=99
# print(list)

# list=['banana','apple','strawberry','wildberry']
# list.append('watermelon')
# print(list)
# list.remove('apple')
# print(list)
# print(len(list))

# list=[10,20,30,40,50]
# print(sum(list))
# print(list[::-1])

# list=[]
# for i in range(5):
#     a=int(input())
#     list.append(a)
# print(list, min(list), max(list))

# size=5
# board=[["."]*size for _ in range(size)]
# print(board)

size = 5
board = [["."] * size for _ in range(size)]
print(board)

# for row in board:
#     print(row)
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         print(board[i][j], end=' ')
#     print()

# def print_board(board):
#     for row in board:
#         print(' '.join(row))
#
# s = [
#     ['1', '0', '1', '0'],
#     ['1', '0', '1', '0'],
#     ['1', '0', '1', '0']
# ]
# print_board(s)

# def print_board_2(board):
#     for row in board:
#         print(' '.join(map(str,row)))
#
# a=[
#     [1,3,45,2],
#     [1,23,1,1],
#     [1,3,45,2],
# ]
# print_board_2(a)


# def print_board_3(board):
#     for row in board:
#         print(" ".join(str(x) for x in row))
# a=[
#     [1,3,45,2],
#     [1,23,1,1],
#     [1,3,45,2],
# ]
# print_board_3(a)

# def print_board(board):
#     for row in board:
#         print(" ".join(f"{x:4}" for x in row))
# a=[
#     [12,3,45,2],
#     [11,23,1,1],
#     [14,3,45,2],
# ]
# print_board(a)

# def print_board(board):
#     print("     " + "    ".join(str(i+1) for i in range(len(board[0]))))  # номера столбцов
#     print()
#     for i, row in enumerate(board):
#         print(f"{i+1}  " + " ".join(f'{x:4}' for x in row))
# a=[
#     [12,3,45,2],
#     [11,23,1,1],
#     [14,3,45,2],
# ]
# print_board(a)

# try:
#     число = int(input("Введите число от 1 до 8: "))
#     print("Вы ввели:", число)
# except ValueError:
#     print("Ошибка! Нужно ввести число от 1 до 8.")

# try:
#     move = int(input("Введите номер строки (0-2): "))
#     if move < 0 or move > 2:
#         print("Число вне диапазона!")
#     else:
#         print("Ваш ход:", move)
# except ValueError:
#     print("Ошибка! Нужно ввести число.")


# def get_int(prompt, min_value, max_value):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value < min_value or value > max_value:
#                 print(f"Введите число от {min_value} до {max_value}.")
#             else:
#                 return value
#         except ValueError:
#             print("Ошибка! Нужно ввести число.")
# row = get_int("Введите номер строки (0-2): ", 0, 2)
# col = get_int("Введите номер столбца (0-2): ", 0, 2)
# print(f"Ваш ход: строка {row}, столбец {col}")

# def is_valid_row(board, row):
#     """
#     Проверяет, есть ли фишки в выбранной строке.
#     """
#     return any(cell == 1 for cell in board[row])

# def is_valid_col(board, col):
#     """
#     Проверяет, есть ли фишки в выбранном столбце.
#     """
#     return any(board[r][col] == 1 for r in range(len(board)))

# def get_valid_row(board):
#     while True:
#         row = get_int("Введите номер строки: ", 1, len(board))
#         if is_valid_row(board, row):
#             return row
#         else:
#             print("В этой строке нет фишек! Попробуйте снова.")











