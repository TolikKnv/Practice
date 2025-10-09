def calc():
    num1 = float(input('Введите первое число: '))
    el=input('Введите действие: ')
    num2 = float(input('Введите второе число: ')) 
    if el == '+':
        rez=num1+num2
    elif el == '-':
        rez=num1-num2
    elif el == '*':
        rez=num1*num2
    elif el == '/':
        rez=num1/num2
    s=input('Если хотите закончить напишите "всё": ')
    while s!='всё':
        num3=float(input('Введите число: '))
        el = input('Введите действие: ')
        if el == '+':
            rez += num3
        elif el == '-':
            rez -= num3
        elif el == '*':
            rez *= num3
        elif el == '/':
            rez /= num3
        s = input('Если хотите закончить напишите "всё": ')
    print(rez)

calc()

