import csv
def func(name1, name2):
    with open(name1, 'r', encoding='utf-8') as f:
        rez1 = f.read()
    rez = rez1.split()
    print(rez)
    with open(name2, 'r', encoding='IBM866') as f1:
        file = csv.reader(f1, delimiter=';')
        for i in file:
            print(i)



func(r'C:\Users\Honor\Desktop\Работа с файлами\10.12.txt',r'C:\Users\Honor\Desktop\Работа с файлами\10.12.csv')