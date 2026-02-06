# 2

a1 = (15, 10, 5)
a2 = (3, 1)
a3 = [2, 35, 55]
a4 = (5, 10, 15, 20)


def prod(a, b=1, c=1):
    return a * b * c


# print(prod(*a4[:3]))


# 3
def prod_1(*args):
    k = 1
    for i in range(len(args)):
        k *= args[i]

    return k


print(prod_1(1, 2, 3, 4, 5, 6, 7))
