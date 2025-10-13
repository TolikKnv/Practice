from math import *
from itertools import count

does = {"плюс": "+", "минус": "-", "умножить": "*", "разделить": "/"}

scobs = {"left": "(", "right": ")"}

numbers = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
    "сто": 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900,
    "одна тысяча": 1000,
    "две тысячи": 2000,
    "три тысячи": 3000,
    "четыре тысячи": 4000,
    "пять тысяч": 5000,
    "шесть тысяч": 6000,
    "семь тысяч": 7000,
    "восемь тысяч": 8000,
    "девять тысяч": 9000,
}

numbers_int = {}

for k, v in numbers.items():
    k, v = v, k
    numbers_int[k] = v

vur = input("Введите выражение: ")
nach = vur
vur = vur.lower()
vur = vur.replace("умножить на", "умножить")
vur = vur.replace("разделить на", "разделить")
vur = vur.replace("скобка открывается", "left")
vur = vur.replace("скобка закрывается", "right")
print(vur)
vur = vur.split()
sum = ""
chi = 0
for i in range(len(vur)):
    if vur[i] in numbers:
        ind=i
        while vur[ind-1] in numbers:
            chi += numbers[vur[ind-1]]
            ind+=1
        if chi>0:
            sum+=str(chi)
        chi=0
    elif vur[i] in scobs:
        sum += scobs[vur[i]]
    else:
        sum += does[vur[i]]

print(eval(sum))
sum = eval(sum)


def kon(sum):
    otv = ""
    if sum < 0:
        otv = "минус "
        sum = sum * (-1)
    if sum % 100 < 20 and sum < 100:
        otv += numbers_int[sum]
    elif sum % 100 < 20 and sum > 100:
        sum = str(sum)
        l = []
        l.extend(sum)
        for i in range(len(l) - 2):
            if numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] != "ноль":
                otv += numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] + " "
                otv = otv[:-1] + numbers_int[int(l[-2] + l[-1])]
            if sum == "0":
                otv = "ноль"
    else:
        sum = str(sum)
        l = []
        l.extend(sum)
        for i in range(len(l)):
            if numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] != "ноль":
                otv += numbers_int[int(l[i]) * 10 ** (len(l) - i - 1)] + " "
        otv = otv[:-1]
        if sum == "0":
            otv = "ноль"

    print(nach + "=" + otv, sep=" ")


kon(sum)
