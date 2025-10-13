l=['(',23,'+',32,')','*',3,'-',1]



def to_rpn(tokens):
    # Приоритет операторов: * выше, чем + и -
    ops_priority = {"+": 1, "-": 1, "*": 2}

    output = []  # список для выходной (постфиксной) записи
    stack = []   # стек для временного хранения операторов и скобок

    # Проходим по каждому токену (числу, оператору или скобке)
    for t in tokens:
        # Если токен — число, сразу добавляем его в выходной список
        if isinstance(t, int):
            output.append(t)

        # Если токен — оператор (+, -, *), обрабатываем приоритет
        elif t in ops_priority:
            # Пока на вершине стека оператор с большим или равным приоритетом —
            # выталкиваем его в выходную очередь
            while (
                stack
                and stack[-1] in ops_priority
                and ops_priority[stack[-1]] >= ops_priority[t]
            ):
                output.append(stack.pop())
            # Кладём текущий оператор в стек
            stack.append(t)

        # Если токен — открывающая скобка, просто помещаем её в стек
        elif t == "(":
            stack.append(t)

        # Если токен — закрывающая скобка, выталкиваем всё до открывающей
        elif t == ")":
            # Переносим операторы из стека в выход, пока не встретим "("
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # удаляем "(" из стека (но не добавляем в выход)

    # После обработки всех токенов выталкиваем оставшиеся операторы
    while stack:
        output.append(stack.pop())

    return output  # Возвращаем выражение в виде обратной польской нотации (RPN)


def eval_rpn(rpn):
    # Стек для вычислений
    stack = []

    # Проходим по каждому токену в постфиксной записи
    for token in rpn:
        # Если токен — число, кладём его в стек
        if isinstance(token, (int, float)):
            stack.append(token)

        # Если токен — оператор, извлекаем два верхних числа и применяем операцию
        elif token in ["+", "-", "*"]:
            b = stack.pop()  # второе число
            a = stack.pop()  # первое число
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)

    # В конце в стеке остаётся один элемент — результат вычисления
    return stack[0]

print(eval_rpn(to_rpn(l)))