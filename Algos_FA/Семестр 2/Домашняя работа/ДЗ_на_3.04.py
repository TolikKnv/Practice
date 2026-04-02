ot = 0


def printIn(s):
    global ot
    print("    " * ot + s)
    ot += 1


def printOut(s):
    global ot
    ot -= 1
    print("    " * ot + str(s))
    return s


def factorial_iter(n):
    if n < 0:
        raise ValueError("n должно быть >= 0")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# 2) факториал через рекурсию + отладка
def factorial(n):
    if n < 0:
        raise ValueError("n должно быть >= 0")

    printIn(f"factorial({n})")

    if n == 0:
        return printOut(1)

    result = n * factorial(n - 1)
    return printOut(result)



print(factorial(4))

print(factorial_iter(4))