# Реализовать декоратор с именем not_none, который генерирует
# исключительную ситуацию если декорируемая функция вернула значения None.

def not_none(func):
    def wrapper(a):
        result = func(a)
        assert result != None, 'Исключение'
        return result

    return wrapper


@not_none
def func(a):
    if a:
        return 'NO Исключение'


print(func(2))
