def decor(func):
    def wrapper(*args):
        try:
            for item in args:
                if isinstance(item, int):
                    continue
                else:
                    raise TypeError
            return sum(args)
        except TypeError:
            return f'NO'
    return wrapper

@decor
def func(a,b):
    return a+b

print(func(2,3))