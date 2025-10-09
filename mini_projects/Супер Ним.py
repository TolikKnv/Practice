import random

size = 8
board = [[1] * size for _ in range(size)]


def board_gen(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = random.randint(0, 1)
    print_board(board)


def print_board(board):
    print("    " + "  ".join(str(i + 1) for i in range(len(board[0]))))
    print()
    for i, row in enumerate(board):
        print(f"{i + 1}  " + " ".join(f"{x:2}" for x in row))


def move_1(prm):
    while True:
        try:
            global move
            move = input(prm)
            if move not in ["столбец", "строка"]:
                print("Не корректный ввод")
            else:
                return move
        except ValueError:
            print("Ошибка! Введите 'строка' или 'столбец'")


def valid_row(board, row):
    return any(cell == 1 for cell in board[row])


def valid_col(board, col):
    return any(board[r][col] == 1 for r in range(len(board)))


def move_2(prm_1, prm_2, min_value, max_value):
    if move in ["строка", "строке"]:
        while True:
            try:
                global change
                change = int(input(prm_1))
                if change < min_value or change > max_value:
                    print(f"Строки нет в диапазоне от {min_value} до {max_value}")
                elif valid_row(board, change - 1):
                    return change
                else:
                    print("В этой строке нет фишек! Попробуйте снова.")
            except ValueError:
                print(f"Ошибка! Введите число от {min_value} до {max_value}")
    elif move in ["столбец", "столбце"]:
        while True:
            try:
                change = int(input(prm_2))
                if change < min_value or change > max_value:
                    print(f"Столбца нет в диапазоне от {min_value} до {max_value}")
                elif valid_col(board, change - 1):
                    return change
                else:
                    print("В этом столбце нет фишек! Попробуйте снова.")
            except ValueError:
                print(f"Ошибка! Введите число от {min_value} до {max_value}")


def board_change(board):
    if move == "строка":
        for i in range(len(board[change - 1])):
            board[change - 1][i] = 0
    elif move == "столбец":
        for i in range(len(board)):
            board[i][change - 1] = 0
    print_board(board)


def game_over(board):
    return all(all(cell == 0 for cell in row) for row in board)


board_gen(board)
player = 1

while True:
    print(f"\nХод игрока {player}")
    move_1("Выберите 'строка' или 'столбец': ")
    move_2("Введите номер строки: ", "Введите номер столбца: ", 1, size)
    board_change(board)

    if game_over(board):
        print(f"\nИгра окончена! Победил игрок {player}")
        break

    player = 2 if player == 1 else 1
