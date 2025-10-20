import random  # Импортируем модуль random для генерации случайных чисел

size = 8  # Размер игрового поля (8x8)
board = [[1] * size for _ in range(size)]  # Создаём поле, заполненное единицами (фишками)


def board_gen(board):
    """Генерирует случайное расположение фишек (0 или 1) на доске"""
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = random.randint(0, 1)  # Каждая ячейка получает случайное значение 0 или 1
    print_board(board)  # Выводим доску на экран


def print_board(board):
    """Выводит игровое поле в удобном для чтения формате"""
    print("    " + "  ".join(str(i + 1) for i in range(len(board[0]))))  # Номера столбцов
    print()
    for i, row in enumerate(board):
        print(f"{i + 1}  " + " ".join(f"{x:2}" for x in row))  # Номера строк и содержимое


def move_1(prm):
    """Запрашивает у игрока, хочет ли он выбрать строку или столбец"""
    while True:
        try:
            global move
            move = input(prm)  # Пользователь вводит "строка" или "столбец"
            if move not in ["столбец", "строка"]:
                print("Не корректный ввод")  # Если ввод неверный — просим повторить
            else:
                return move  # Возвращаем корректный выбор
        except ValueError:
            print("Ошибка! Введите 'строка' или 'столбец'")


def valid_row(board, row):
    """Проверяет, есть ли хотя бы одна фишка (1) в строке"""
    return any(cell == 1 for cell in board[row])


def valid_col(board, col):
    """Проверяет, есть ли хотя бы одна фишка (1) в столбце"""
    return any(board[r][col] == 1 for r in range(len(board)))


def move_2(prm_1, prm_2, min_value, max_value):
    """
    Запрашивает у игрока номер строки или столбца.
    Проверяет корректность ввода и наличие фишек.
    """
    if move in ["строка", "строке"]:
        while True:
            try:
                global change
                change = int(input(prm_1))  # Ввод номера строки
                if change < min_value or change > max_value:
                    print(f"Строки нет в диапазоне от {min_value} до {max_value}")
                elif valid_row(board, change - 1):
                    return change  # Возвращаем номер, если в строке есть фишки
                else:
                    print("В этой строке нет фишек! Попробуйте снова.")
            except ValueError:
                print(f"Ошибка! Введите число от {min_value} до {max_value}")
    elif move in ["столбец", "столбце"]:
        while True:
            try:
                change = int(input(prm_2))  # Ввод номера столбца
                if change < min_value or change > max_value:
                    print(f"Столбца нет в диапазоне от {min_value} до {max_value}")
                elif valid_col(board, change - 1):
                    return change  # Возвращаем номер, если в столбце есть фишки
                else:
                    print("В этом столбце нет фишек! Попробуйте снова.")
            except ValueError:
                print(f"Ошибка! Введите число от {min_value} до {max_value}")


def board_change(board):
    """Обнуляет (удаляет) фишки в выбранной строке или столбце"""
    if move == "строка":
        for i in range(len(board[change - 1])):
            board[change - 1][i] = 0  # Обнуляем всю строку
    elif move == "столбец":
        for i in range(len(board)):
            board[i][change - 1] = 0  # Обнуляем весь столбец
    print_board(board)  # Печатаем обновлённое поле


def game_over(board):
    """Проверяет, закончилась ли игра (все фишки удалены)"""
    return all(all(cell == 0 for cell in row) for row in board)


# Генерируем случайное игровое поле
board_gen(board)
player = 1  # Начинает игрок 1

# Основной игровой цикл
while True:
    print(f"\nХод игрока {player}")
    move_1("Выберите 'строка' или 'столбец': ")  # Выбор направления
    move_2("Введите номер строки: ", "Введите номер столбца: ", 1, size)  # Ввод номера
    board_change(board)  # Обновляем доску

    if game_over(board):  # Проверка конца игры
        print(f"\nИгра окончена! Победил игрок {player}")
        break

    # Меняем игрока (1 → 2 → 1 ...)
    player = 2 if player == 1 else 1
