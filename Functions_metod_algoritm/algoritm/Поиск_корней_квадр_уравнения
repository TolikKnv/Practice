from math import *


def corner_find():
    a = float(input())
    b = float(input())
    c = float(input())
    disc = b**2 - 4 * a * c
    if disc < 0:
        print("Нет корней")
    elif disc == 0:
        print(-b / (2 * a))
    else:
        lum = []
        lum += [(-b + sqrt(disc)) / (2 * a)]
        lum += [(-b - sqrt(disc)) / (2 * a)]
        lum.sort()
        print(*lum, sep="\n")


corner_find()
