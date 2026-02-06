# 2
# a
# a = int(input())
# func = lambda x: x*a
# print(func(int(input())))


# b
# l = [13, 121, 19, 23, 25, 39, 2134, 26]
# q = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, l))
# print(q)


# c
# l = [1.0, 23, 2.12, 22, 3.01, 3, 23.0123]
# q = sum(map(lambda x: 1 if isinstance(x,float) else 0,l))
# print(q)


# 3
# a

# l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# q = sorted(l, key=lambda x: x[1])
# print(q)


# b
# l = ["aba", "qwe", "zoz", "sdsdssa", "asasa", "qazs", "qweeedc"]
# q = list(filter(lambda x: x == x[::-1], l))
# print(q)


#c
# l = [13, 121, 19, 23, 25, 39, 2134, 26]
# q = set(map(lambda x: (l.index(x),x) if x in [max(l), min(l)] else False, l))
# print(q)