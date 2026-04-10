# 3
def sleit(*a):
    """СКЛЕИТЬ текст"""

    return " ".join(a)


def summa(a, b):
    """сумма"""
    return a + b


def razn(a, b):
    """разность"""
    return a - b


def proizv(a, b):
    """произвдедение"""
    return a * b


def func(*a):
    d = dict()

    for i in a:
        d[i.__doc__.split()[0]] = i

    return d


# def repl(com):
#     a = input("введите функцию")
#     if a == "сумма":

#         print(q["сумма"](2, 3))


q = func(summa, razn, proizv, sleit)
print(q)
for i, j in q.items():
    if i == "СКЛЕИТЬ":
        print()
print(q)
while True:
    a = input("введите функцию")
    if a == "сумма":
        print(q["сумма"](2, 3))
    if a.split()[0] == "СКЛЕИТЬ":
        print(a.split()[0], q["СКЛЕИТЬ"]('one', 'two', 'three'))

    if a == "":
        break
