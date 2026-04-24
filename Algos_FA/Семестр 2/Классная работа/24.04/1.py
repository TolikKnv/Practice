from functools import reduce

# 1
# l = [3,5,23,5,-3,6]
# rez = list(filter(lambda q:q, list(map(lambda x:(x, l.index(x)) if x == max(l) or x == min(l) else 0, l))))
# print(*rez)


# 2
# a = ['ahdfs', 'qwe', 'aDg', 'gHd']
# rez = reduce(lambda q,w: q+w, filter(lambda x:x.upper() if x[0] in 'Aa' else 0, a))
# print(rez)

# 3.1
# l = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
# 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# rez = list(reversed(sorted(l, key = lambda el: int(el['model']))))
# print(rez)

# 3.2
# el = 'abcd'
# l = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# rez = list(filter(lambda x: sorted(x) == sorted(el), l))
# print(rez)

# 3.3
# l = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# rez = list(sorted(l, key = lambda x: (isinstance(x, str), x)))
# print(rez)

# 12
# l = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
# rez1 = reduce(lambda q,w:q+w, map(lambda x: 1 if x > 0 else 0, l))
# rez2 = reduce(lambda q,w:q+w, map(lambda x: 1 if x < 0 else 0, l))
# rez3 = reduce(lambda q,w:q+w, map(lambda x: 1 if x == 0 else 0, l))
# print(rez1/len(l), rez2/len(l), rez3/len(l))


# 13
# l = ["a", "b", "E", "f", "a", "i", "o", "U", "a"]
# rez = set(filter(lambda q:q, list(map(lambda x:(x.upper(), x.lower()), l))))
# print(rez)

#14
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return fib[:n]


# fib_numbers = fibonacci(10)
# squares = list(map(lambda x: x**2, fib_numbers))

# print(squares)

from itertools import islice

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


N = 1134

squares = list(map(lambda x: x**2, islice(fib(), N)))

print(squares)