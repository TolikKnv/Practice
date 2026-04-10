def new_print(func):
    def wrapper(*args):
        result = func(*args)
        print(result)

    return wrapper


@new_print
def func(a,b):
    return a+b, a-b
func(2,3)