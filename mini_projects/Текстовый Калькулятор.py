from math import *
from itertools import count

does = {" плюс ": "+", " минус ": "-", " умножить на ": "*"}

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


def calc():
    vur = input("Введите выражение: ")
    vur = vur.lower()
    if " плюс " in vur:
        vur_num = vur.split(" плюс ")
        chi = vur_num[0].split() + vur_num[1].split()
        sum = 0
        for i in range(len(chi)):
            sum += numbers[chi[i]]

        if sum%100<20 and sum<100:
            otv = numbers_int[sum]
        elif sum%100<20 and sum>100:
            sum = str(sum)
            l = []
            l.extend(sum)
            otv = ''
            for i in range(len(l)-2):
                if numbers_int[int(l[i])*10**(len(l)-i-1)] !='ноль':
                    otv += numbers_int[int(l[i])*10**(len(l)-i-1)]+' '
            otv = otv[:-1]+numbers_int[int(l[-2]+l[-1])]
            if sum == '0':
                otv = 'ноль'
        else:
            sum = str(sum)
            l = []
            l.extend(sum)
            otv = ''
            for i in range(len(l)):
                if numbers_int[int(l[i])*10**(len(l)-i-1)] !='ноль':
                    otv += numbers_int[int(l[i])*10**(len(l)-i-1)]+' '
            otv = otv[:-1]
            if sum == '0':
                otv = 'ноль'



    if " минус " in vur:
        vur_num = vur.split(" минус ")
        chi = vur_num[0].split()
        chi2 = vur_num[1].split()
        sum = 0
        for i in range(len(chi)):
            sum += numbers[chi[i]]
        for i in range(len(chi2)):
            sum -= numbers[chi2[i]]


        if sum%100<20 and sum<100:
            otv = numbers_int[sum]
        elif sum%100<20 and sum>100:
            sum = str(sum)
            l = []
            l.extend(sum)
            otv = ''
            for i in range(len(l)-2):
                if numbers_int[int(l[i])*10**(len(l)-i-1)] !='ноль':
                    otv += numbers_int[int(l[i])*10**(len(l)-i-1)]+' '
            otv = otv[:-1]+numbers_int[int(l[-2]+l[-1])]
            if sum == '0':
                otv = 'ноль'
        else:
            sum = str(sum)
            l = []
            l.extend(sum)
            otv = ''
            for i in range(len(l)):
                if numbers_int[int(l[i])*10**(len(l)-i-1)] !='ноль':
                    otv += numbers_int[int(l[i])*10**(len(l)-i-1)]+' '
            otv = otv[:-1]
            if sum == '0':
                otv = 'ноль'

    if " умножить на " in vur:
        vur_num = vur.split(" умножить на ")
        chi1 = vur_num[0].split()
        chi2 = vur_num[1].split()
        wer, wer1 = 0, 0
        for i in range(len(chi1)):
            wer += numbers[chi1[i]]
        for i in range(len(chi2)):
            wer1 += numbers[chi2[i]]
        sum = wer1 * wer
        sum = str(umn)

        l = []
        l.extend(umn)
        otv = ''
        for i in range(len(l)):
            if numbers_int[int(l[i])*10**(len(l)-i-1)] !='ноль':
                otv += numbers_int[int(l[i])*10**(len(l)-i-1)]+' '
        otv = otv[:-1]
        if umn == '0':
            otv = 'ноль'


    print(f"{vur}" + " = " + otv, sep=" ")


calc()
