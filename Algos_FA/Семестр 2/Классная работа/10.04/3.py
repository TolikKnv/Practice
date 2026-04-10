def new_print(func):
    def wrapper(*args):
        result = func(*args)
        return(result[0][::-1], str(result[1])[::-1])
    return wrapper


@new_print
def func(a,b):
    return a,b
print(func('asd', 12))