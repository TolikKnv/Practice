# a = [5, -6, 7, 3, 51, 8]
# b = sum([i for i in a if i > 0])
# print(b)


# 4
# def summa(a, b):
#     return a + b


# def razn(a, b):
#     return a - b


# def umn(a, b):
#     return a * b


# def div(a, b):
#     return a / b


# d = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b,
# }


# def func(a, b, op):
#     return d[op](a, b)


# print(func(25, 4, "+"))


# 1
# a = lambda a, b, h: (a + b) * h / 2
# ans = a(10, 20, 5)
# print(ans)


# 3
# PI = 3.14
# S = 20
# rad = lambda : [(S//PI)**0.5, (S//PI)**0.5*PI*2]
# radius = rad()
# print(radius)


# 4
# dl = [{"a": 10, "b": 20, "c": 1}, {"a": 5, "b": 10, "z": 10}, {"a": 3, "y": 7}]
# a = sorted(dl, key = lambda x:x['a'])
# print(a)

# 5
# def calc_op(s, oper_d):
#     a, b, op = int(s.split(' ')[0]), int(s.split(' ')[2]), s.split(' ')[1]
#     ans  = lambda a,b,op: oper_d[op](a,b)
#     return ans(a,b,op)
# print(calc_op('2 s 10', {'s': lambda x,y: x**y}))


# 1a
# a = lambda x,y: [15 + x, y*x]
# print(a(10,2))


#1b
# l = [(1,2,3),(4,5,6),(7,8,9)]
# rez_min = list(map(lambda x: min(x), l))
# rez_max = list(map(lambda x: max(x), l))
# min_max = [min(rez_min), max(rez_max)]
# print(rez_min, rez_max, min_max)

#1v
# l = ['dewsd', '123', 'dfre', '234', 'dfghjhgfd', '123']
# a = 3
# rez = list(filter(lambda s: len(s) == a, l))
# print(rez)


