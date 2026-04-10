# С помощью декоратора реализовать отладочный вывод работы
# factorial(n) как для вызовов функций, так и для возвращаемых значений.

ot = 0


def mod_1(func):
    def wrapper(a):
        global ot

        print("    " * ot + f'factorial({a})')
        ot += 1
        result = func(a)
        ot-=1
        return result

    return wrapper

def mod_2(func):
    def wrapper(s):
        result = func(s)
        global ot
        print("    " * ot + str(s))
        return result

    return wrapper





@mod_1
@mod_2
def factorial(n):
    if n < 0:
        raise ValueError("n должно быть >= 0")

    if n == 0:
        return 1

    result = n * factorial(n - 1)
    return result


print(factorial(4))

