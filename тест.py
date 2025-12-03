list = [1, 2, 3, 5, 2.45, 2.543, 1.54, "qwd2", "wefer", "derfe", "wedfr"]

q = sum(map(lambda x: 1 if isinstance(x, float) else 0, list))
print(q)