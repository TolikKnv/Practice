# from functools import cache

import time

start = time.perf_counter()

def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            return storage[args]

        result = func(*args)
        storage[args] = result
        return result

    return wrapper


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

fib(30)
end = time.perf_counter()
print(end - start)
