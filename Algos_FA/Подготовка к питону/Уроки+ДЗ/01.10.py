# l1=['input', 'string', 'repeat', 3]
# l=[]
# try:
#     if 'repeat' in l1 and l1[-1]:
#         l=l1[:-2]*l1[-1]
#         l.append(l1[-2])
#         l.append(l1[-1])
#     print(l)
# except TypeError:
#     print('Последний элемент не число')

# s=input()
# l=[]
# l.extend(s)
# print(l)
# for i in range(1,len(l)-1):
#     if l[i]=='s' or l[i]=='S':
#         l[i]=l[i-1]*2+l[i+1]
# print(l)

# s1=input()
# s2=input()
# ls=[s1,s2]
# ll=[len(s1),len(s2)]
# ldef=['ДО','ПОСЛЕ']
# def leng(st):
#     print(f'Длины строк: {ll[0]} и {ll[1]}')
#
# def order(ls):
#     usl=[ord(c) for c in ls[0]]<[ord(c) for c in ls[1]]
#     print(f"Строка '{ls[0]}' идет {'ПЕРЕД' if usl else 'ПОСЛЕ'} строкой '{ls[1]}'")
#
# g=input('Введите функцию: ')
# if g=='leng':
#     leng(ll)
# if g=='order':
#     order(ls)


