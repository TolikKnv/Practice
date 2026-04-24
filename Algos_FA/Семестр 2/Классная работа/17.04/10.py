def dec(a,b):
    def decor(func):
        def wrapper(*args):
            rez=func(*args)
            if rez>0:
                return rez+a
            elif rez<0:
                return rez-b
        return wrapper
    return decor


@dec(2,1000)
def func(*args):
    s = 0
    for item in args:
        s+=item
    return s

print(func(2,3,4,5,6,7,8,9,-100))