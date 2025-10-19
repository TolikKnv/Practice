def decryption(str, k, alphabet):
    decryption_str = ""  # строка для хранения результата дешифрования
    for i in range(len(str)):  # перебираем каждый символ строки
        # проверяем, является ли символ буквой английского или русского алфавита
        if (
            str[i].lower()
            in "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю"
        ):
            # если буква английская строчная
            if str[i] == str[i].lower() and alphabet == 26:
                decryption_str += chr((ord(str[i]) - k - 97) % alphabet + 97)
            # если буква английская заглавная
            elif str[i] == str[i].upper() and alphabet == 26:
                decryption_str += chr((ord(str[i]) - k - 65) % alphabet + 65)
            # если буква русская строчная
            elif str[i] == str[i].lower() and alphabet == 32:
                decryption_str += chr((ord(str[i]) - k - 1072) % alphabet + 1072)
            # если буква русская заглавная
            elif str[i] == str[i].upper() and alphabet == 32:
                decryption_str += chr((ord(str[i]) - k - 1040) % alphabet + 1040)
        else:
            # если символ не является буквой — добавляем без изменений
            decryption_str += str[i]
    return decryption_str  # возвращаем дешифрованный текст


def encryption(str, k, alphabet):
    encryption_str = ""  # строка для хранения результата шифрования
    for i in range(len(str)):  # перебираем каждый символ строки
        # проверяем, является ли символ буквой английского или русского алфавита
        if (
            str[i].lower()
            in "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю"
        ):
            # если буква английская строчная
            if str[i] == str[i].lower() and alphabet == 26:
                encryption_str += chr((ord(str[i]) + k - 97) % alphabet + 97)
            # если буква английская заглавная
            elif str[i] == str[i].upper() and alphabet == 26:
                encryption_str += chr((ord(str[i]) + k - 65) % alphabet + 65)
            # если буква русская строчная
            elif str[i] == str[i].lower() and alphabet == 32:
                encryption_str += chr((ord(str[i]) + k - 1072) % alphabet + 1072)
            # если буква русская заглавная
            elif str[i] == str[i].upper() and alphabet == 32:
                encryption_str += chr((ord(str[i]) + k - 1040) % alphabet + 1040)
        else:
            # если символ не является буквой — добавляем без изменений
            encryption_str += str[i]
    return encryption_str  # возвращаем зашифрованный текст


def __main__():
    # запрашиваем у пользователя параметры
    action = input("Введите действие (шифрование/дешифрование): ")
    alphabet = input("Введите алфавит(русский/английский): ")
    text = input("Введите текст: ")
    key = int(input("Введите сдвиг: "))

    # определяем длину алфавита (русский — 32, английский — 26)
    if alphabet == "русский":
        alphabet = 32
    else:
        alphabet = 26

    # если выбрано шифрование — вызываем функцию encryption
    if action == "шифрование":
        print(encryption(text, key, alphabet))

    # если выбрано дешифрование — вызываем функцию decryption
    if action == "дешифрование":
        print(decryption(text, key, alphabet))


__main__()  # запуск основной функции программы
