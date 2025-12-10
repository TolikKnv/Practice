import csv
def func(name1, name2):
    with open(name1, encoding='utf-8') as f:
        rez1 = f.read().split()
    print(rez1)
    with open(name2) as f1:
        file = csv.reader(f1, delimiter=';')
    for i in file:
        print(i)



func('text.txt','10.12.csv')