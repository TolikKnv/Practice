# Реализовать декоратор с именем print_type, выводящий на
# печать тип значения, возвращаемого декорируемой функцией.

def print_type(func):
    def wrapper(a):
        result = func(a)
        return type(result)

    return wrapper


@print_type
def func(a):
    return a


print(func({'asd':'qwrrq'}))
