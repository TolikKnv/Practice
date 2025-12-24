import csv


def func(name1, name2):
    with open(name1, encoding="utf-8") as f:
        rez = f.read().split()
    print(rez)
    a = []
    with open(name2, encoding="windows-1251") as f1:
        file = csv.reader(f1, delimiter=";")
        for i in file:
            a.append(i)
    print(a)
    name3 = name1[:-4] + "_" + name1[-4:]
    with open(name3, "w", encoding="UTF-8") as f2:
        for i in a:
            if i[0].strip() in rez:
                f2.write(i[1] + " ")


func(r"C:\Users\Honor\Downloads\123.txt", r"C:\Users\Honor\Downloads\123.csv")
