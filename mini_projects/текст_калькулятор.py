does = {"плюс": "+", "минус": "-", "умножить": "*"}


brackets = {"left": "(", "right": ")"}

numbers = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
    "сто": 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900,
    "одна тысяча": 1000,
    "две тысячи": 2000,
    "три тысячи": 3000,
    "четыре тысячи": 4000,
    "пять тысяч": 5000,
    "шесть тысяч": 6000,
    "семь тысяч": 7000,
    "восемь тысяч": 8000,
    "девять тысяч": 9000,
}

numbers_int = {}

for k, v in numbers.items():
    k, v = v, k
    numbers_int[k] = v


def words_to_list():
    # Преобразовываем из строки в список с математическими элементами
    vur = input("Введите выражение: ")
    vur = vur.lower()
    global start_str
    start_str = vur
    vur = vur.replace("скобка открывается", "left")
    vur = vur.replace("скобка закрывается", "right")
    vur = vur.replace("умножить на", "умножить")
    vur = vur.split()
    l = []
    for i in vur:
        if i in numbers:
            l.append(numbers[i])
        if i in does:
            l.append(does[i])
        if i in brackets:
            l.append(brackets[i])
        if i not in numbers and i not in does and i not in brackets:
            print("Ошибка: неверный ввод - неизвестные слова.")
            exit()

    # Делаем список, где хранится каждый элемент примера
    sec = []
    for i in range(len(l)):
        if str(l[i]) in "()*-+":
            sec.append(l[i])
        else:
            ind = i
            chi = l[i]
            for j in l[ind + 1 :]:
                if str(j) not in "()+*-":
                    chi += j
                elif len(sec) > 0 and str(sec[-1]) not in "+-*()":
                    break
                else:
                    sec.append(chi)
                    break
    if str(l[-1]) not in "+-*()":
        sec.append(chi)
    return sec


def var_check(expression: list):
    check = ""
    for i in expression:
        check += str(i)
    if check.count("(") != check.count(")"):
        print("Ошибка: несоответствие количества открывающих и закрывающих скобок.")
        exit()
    if expression[0] in does.values():
        print("Ошибка: оператор не может быть первым.")
        exit()
    if expression[-1] in does.values():
        print("Ошибка: оператор не может быть последним.")
        exit()
    for i in range(len(expression) - 1):
        if expression[i] == "(" and expression[i + 1] == ")":
            print("Ошибка: пустые скобки ()")
            exit()
    if (
        "**" in check
        or "++" in check
        or "--" in check
        or "+*" in check
        or "*+" in check
        or "-*" in check
        or "*-" in check
        or "+-" in check
        or "-+" in check
    ):
        print("Ошибка: несколько операторов не может идти подряд.")
        exit()


def to_rpn(tokens):
    ops_priority = {"+": 1, "-": 1, "*": 2}
    output = []
    stack = []

    for t in tokens:
        if isinstance(t, (int)):
            output.append(t)
        elif t in ops_priority:
            while (
                stack
                and stack[-1] in ops_priority
                and ops_priority[stack[-1]] >= ops_priority[t]
            ):
                output.append(stack.pop())
            stack.append(t)
        elif t == "(":
            stack.append(t)
        elif t == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # убираем '('
    while stack:
        output.append(stack.pop())
    return output


def eval_rpn(rpn):
    stack = []
    for token in rpn:
        if isinstance(token, (int, float)):
            stack.append(token)
        elif token in ["+", "-", "*"]:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
    return stack[0]


def convert(sum):
    if sum % 100 < 20 and sum < 100:
        otv = numbers_int[sum]
    elif sum % 100 < 20 and sum > 100:
        sum = str(sum)
        l = []
        l.extend(sum)
        otv = ""
        for i in range(len(l) - 2):
            if numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] != "ноль":
                otv += numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] + " "
        otv = otv[:-1] + " " + numbers_int[int(l[-2] + l[-1])]
        if sum == "0":
            otv = "ноль"
    else:
        sum = str(sum)
        l = []
        l.extend(sum)
        otv = ""
        for i in range(len(l)):
            if numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] != "ноль":
                otv += numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] + " "
        otv = otv[:-1]
        if sum == "0":
            otv = "ноль"
    print(start_str + " = " + otv, sep=" ")


kon = words_to_list()
var_check(kon)
convert(eval_rpn(to_rpn(kon)))
