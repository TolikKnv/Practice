import time


def decor(func):
    def wrapper(a):
        start = time.perf_counter()
        result = func(a)
        assert (
            time.perf_counter() - start < 0.01
        ), "Время выполнения функции меньше 0.1 секунды"
        # print(f"Время выполнения функции: {time.perf_counter() - start} секунд")
        return result

    return wrapper


@decor
def factorial(n):
    if n < 0:
        raise ValueError("n должно быть >= 0")

    if n == 0:
        return 1

    result = n * factorial(n - 1)
    return result


print(factorial(200))
