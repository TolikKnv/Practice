from random import *  # Импортируем все функции из модуля random (choice, shuffle и т.д.)

# Наборы символов для генерации паролей
digits = "0123456789"                      # Цифры
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"  # Строчные буквы
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Прописные (заглавные) буквы
punctuation = "!#$%&*+-=?@^_"              # Специальные символы

# Ввод параметров генерации от пользователя
quantity_of_passwords = int(input("Какое количество паролей надо сгенерировать?: "))
len_of_password = int(input("Какая длина должна быть у одного пароля?: "))

# Пользователь выбирает, какие символы можно использовать
permission_digits = input("Включать в пароль цифры? - ")
permission_big_letter = input("Включать в пароль прописные буквы? - ")
permission_small_letter = input("Включать в пароль строчные буквы? - ")
permission_symbols = input("Включать в пароль символы? - ")

# Проверяем, что хотя бы один тип символов выбран
while (
    permission_digits == "нет"
    and permission_big_letter == "нет"
    and permission_small_letter == "нет"
    and permission_symbols == "нет"
):
    print('А из чего вообще тогда должен состоять пароль? Укажите хоть где-то "да".')
    # Повторный ввод, если пользователь отключил все категории
    permission_digits = input("Включать в пароль цифры? - ")
    permission_big_letter = input("Включать в пароль прописные буквы? - ")
    permission_small_letter = input("Включать в пароль строчные буквы? - ")
    permission_symbols = input("Включать в пароль символы? - ")


# Функция для создания общего набора допустимых символов
def generation_of_list(a, b, c, d):
    l = ""
    if a == "да":          # Если выбраны цифры
        l += digits
    if b == "да":          # Если выбраны прописные буквы
        l += uppercase_letters
    if c == "да":          # Если выбраны строчные буквы
        l += lowercase_letters
    if d == "да":          # Если выбраны спецсимволы
        l += punctuation
    return l


# Формируем список всех возможных символов для генерации
main_list = []
main_list.extend(
    generation_of_list(
        permission_digits,
        permission_big_letter,
        permission_small_letter,
        permission_symbols,
    )
)
shuffle(main_list)  # Перемешиваем символы для случайности

print()  # Просто пустая строка для красоты вывода

# Генерируем нужное количество паролей
password_list = []
for _ in range(quantity_of_passwords):
    password = ""
    for _ in range(len_of_password):
        password += choice(main_list)  # Добавляем случайный символ из списка
    password_list.append(password)     # Сохраняем пароль в общий список

# Выводим все сгенерированные пароли построчно
print(*password_list, sep="\n")
