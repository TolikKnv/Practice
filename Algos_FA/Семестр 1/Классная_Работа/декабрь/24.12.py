# def repl(st, **kwargs):
#     for i in kwargs:
#         if i in st:
#             st = st.replace(i, kwargs[i])
#     print(st)

# repl('replace my val abc', my='s1', abc='fff')


import csv
with open(r'C:\Users\Honor\Desktop\24.12.csv', 'r', encoding='IBM866') as f:
    rez = csv.reader(f)
    head = next(rez)
    print(head)
    a = []
    for i in rez:
        a.append(i[0].split(';'))
print(a)
with open('new.txt', 'w', encoding='UTF-8') as f1:
    f1.write(f'Файл new.txt содержит {len(head)} столбцов. Имена столбцов {head}.')