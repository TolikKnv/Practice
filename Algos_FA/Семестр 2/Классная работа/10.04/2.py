def new_print(func):
    def wrapper(*args):
        result = func(*args)
        print(result*3, sep=' ')

    return wrapper

a = input()
@new_print
def func(a):
    return a
func(a)