import math
from itertools import count

does = {" плюс ": "+", " минус ": "-", " умножить ": "*"}

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
    "одинадцать": 11,
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
    "две тысяча": 2000,
    "три тысяча": 3000,
    "четыре тысяча": 4000,
    "пять тысяча": 5000,
    "шесть тысяча": 6000,
    "семь тысяча": 7000,
    "восемь тысяча": 8000,
    "девять тысяча": 9000,
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
        if sum >= 100 and sum % 100 >= 20 and sum % 10 != 0:
            otv = f"{numbers_int[sum//100*100]} {numbers_int[sum%100//10*10]} {numbers_int[sum%100%10]}"
        if sum >= 100 and sum % 100 >= 20 and sum % 10 == 0:
            otv = f"{numbers_int[sum//100*100]} {numbers_int[sum%100//10*10]}"
        elif sum >= 100 and 0 < sum % 100 < 20:
            otv = f"{numbers_int[sum // 100*100]} {numbers_int[sum % 100]}"
        elif 20 < sum < 100 and sum % 10 > 0:
            otv = f"{numbers_int[sum//10*10]} {numbers_int[sum%10]}"
        elif 20 < sum < 100 and sum % 10 == 0:
            otv = f"{numbers_int[sum]}"
        elif sum < 20 and sum % 10 != 0:
            otv = f"{numbers_int[sum]}"

    if " минус " in vur:
        vur_num = vur.split(" минус ")
        chi = vur_num[0].split()
        chi2 = vur_num[1].split()
        sum = 0
        for i in range(len(chi)):
            sum += numbers[chi[i]]
        for i in range(len(chi2)):
            sum -= numbers[chi2[i]]
        if (20 >= sum >= 0) or (sum > 20 and sum % 10 == 0):
            otv = f"{numbers_int[sum]}"
        elif sum > 20 and sum % 10 != 0:
            otv = f"{numbers_int[sum//10*10]} {numbers_int[sum%10]}"
        elif (-20 <= sum < 0) or (sum < 0 and sum * (-1) % 10 == 0):
            otv = f"минус {numbers_int[sum*(-1)]}"
        elif -100 <= sum < -20 and sum * (-1) % 10 == 0:
            otv = f"минус {numbers_int[sum * (-1)]}"
        elif -100 < sum < -20 and sum * (-1) % 10 != 0:
            otv = f"минус {numbers_int[sum*(-1)//10*10]} {numbers_int[sum*(-1)%10]}"
        elif sum < -100 and sum * (-1) % 100 >= 20 and sum * (-1) % 10 != 0:
            otv = f"минус {numbers_int[sum*(-1) // 100 * 100]} {numbers_int[sum*(-1) % 100 // 10 * 10]} {numbers_int[sum*(-1) % 100 % 10]}"
        elif sum * (-1) >= 100 and sum * (-1) % 100 >= 20 and sum * (-1) % 10 == 0:
            otv = f"минус {numbers_int[sum*(-1)//100*100]} {numbers_int[sum*(-1)%100//10*10]}"
        elif sum * (-1) >= 100 and 0 < sum * (-1) % 100 < 20:
            otv = f"минус {numbers_int[sum*(-1) // 100*100]} {numbers_int[sum*(-1) % 100]}"

    # if " умножить на " in vur:
    #     vur_num = vur.split(" умножить на ")
    #     chi1 = vur_num[0].split()
    #     chi2 = vur_num[1].split()
    #     wer, wer1 = 0, 0
    #     for i in range(len(chi1)):
    #         wer += numbers[chi1[i]]
    #     for i in range(len(chi2)):
    #         wer1 += numbers[chi2[i]]
    #     umn = wer1 * wer
    #     umn = str(umn)
    #     # if (umn<=20) or (umn<100 and umn%10==0) or (100<=umn<=900 and umn%100==0) or (1000<=umn<=9000 and umn%100==0)
    #     l = []
    #     l.extend(umn)
    #     print(l)

    print(f'{vur}'+' = '+otv, sep=' ')


calc()
