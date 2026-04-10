#  Реализовать декоратор с именем not_sum, который генерирует исключительную ситуацию, если
#  декорируемая функция вернула отрицательное значение суммы трех чисел.

def not_sum(func):
    def wrapper(*a):
        result = func(*a)
        assert result > 0, '<0'
        return result

    return wrapper


@not_sum
def func(a,b,c):
        return a+b+c


print(func(2,3,-100))
