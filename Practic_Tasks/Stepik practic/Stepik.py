# n=int(input())
# output=''
# for i in range(n):
#     s=input()
#     if s.isspace() is True or s=='':
#         output+=f'{i+1}: COMMENT SHOULD BE DELETED\n'
#     else:
#         output+=f'{i+1}: {s}\n'
# print(output)
from numpy.ma.extras import average

# nik=input()
# if nik[0]=='@' and 5<=len(nik)<=15 and nik[1:].isalnum() is True and (nik[1:].islower() is True or nik[1:].isdigit() is True):
#     print('Correct')
# else:
#     print('Incorrect')

# num=input()
# if len(num)==9 and num[0] in 'АВЕКМНОРСТУХ' and num[4] in 'АВЕКМНОРСТУХ' and num[5] in 'АВЕКМНОРСТУХ' and num[1] in '0123456789' and num[3] in '0123456789' and num[3] in '0123456789' and num[6]=='_' and num[7] in '0123456789' and num[8] in '0123456789':
#     print('YES')
# elif len(num) == 10 and num[0] in 'АВЕКМНОРСТУХ' and num[4] in 'АВЕКМНОРСТУХ' and num[5] in 'АВЕКМНОРСТУХ' and num[1] in '0123456789' and num[3] in '0123456789' and num[3] in '0123456789' and num[6] == '_' and num[7] in '0123456789' and num[8] in '0123456789' and num[9] in '0123456789':
#     print('YES')
# else:
#     print('NO')

# a=int(input())
# b=int(input())
# print(f'''
# Для чисел {a} и {b}:
#   Сумма кубов: {a}**3 + {b}**3 = {a**3 + b**3}
#   Куб суммы: ({a} + {b})**3 = {(a + b)**3}
# '''
#     )

# day = int(input())
# weight = float(input())
# step = 0.3
# if weight<=100-step*day:
#     print('Все идет по плану')
#     print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100-step*day} кг')
# else:
#     print('Что-то пошло не так')
#     print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - step * day} кг')

# a=input()
# if a!='Я':
#     print(chr(ord(a)+1))
# else:
#     print('Дальше букв нет')

# world = input()
# for i in range(0,len(world)):
#     print(ord(world[i]),end=" ")


# max=-100000000000000000
# sl=''
# sum = 0
# for i in range(4):
#     a = input()
#     for j in range(len(a)):
#        sum+=ord(a[j])
#     if sum>max:
#         sl=a
#     sum=0
# print(sl)

# fr = input()
# sum=0
# for i in fr:
#     sum+=ord(i)
# print(f"Текст сообщения: '{s}'")
# print(f'Стоимость сообщения: {sum*3}🐝')

# fr=input()
# eng='eyopaxcETOPAHXCBM'
# rus='еуорахсЕТОРАНХСВМ'
# sum1=0
# sum2=0
# for i in fr:
#     sum1+=ord(i)
# sum2=sum1
# for i in fr:
#     if i in eng:
#         ind=eng.find(i)
#         sum2=sum2-ord(i)+ord(rus[ind])
# print(f'Старая стоимость: {sum1}🐝')
# print(f'Новая стоимость: {sum2}🐝')

# step=int(input())
# fr = input()
# for i in fr:
#     print(chr(ord(i)-step+26),end='')

# str = input()
# for i in range (64):
#     sl = ord('А')+i
#     # print(sl)
#     str=str.replace(f'[u-{ord('А')+i}]', chr(ord('А')+i))
# print(str)

# a=input()
# a1=input()
# a2=input()
# a3=input()
# ma=max(a,a1,a2,a3)
# mi=min(a,a1,a2,a3)
# print((ord(ma[-1])*ord(mi[-1]))**3)

# ma='0'
# mi='⬆️'
# s=input()
# while s!='КОНЕЦ':
#     if s>ma:
#         ma=s
#     if s<mi:
#         mi=s
#     s=input()
# print(f'Минимальная строка ⬇️: {mi}')
# print(f'Максимальная строка ⬆️: {ma}')

# a=input().islower()
# b=input().islower()
# for i in a:
#     if i not in 'qwertyuiopasdfghjklzcbnmйцукенгшщзхъфывапролджэячсмитьбюё':
#         a=a.replace(i,'')
# for i in b:
#     if i not in 'qwertyuiopasdfghjklzcbnmйцукенгшщзхъфывапролджэячсмитьбюё':
#         b=b.replace(i,'')
# if a==b:
#     print("YES")
# else:
#     print("NO")

# n=int(input())
# output=''
# for i in range(n):
#     s=input()
#     if len(s)==3 and s[0] in '0123456789' and s[1] in 'АБВГДЕЖЗИЙКЛМНОП':
#         output+='YES\n'
#     else:
#         output+='NO\n'
# print(output)

# a=input()
# b=input()
# c=input()
# l=[a,b,c]
# mi=min(l)
# ma=max(l)
# for i in range(len(l)):
#     if mi<l[i]<ma:
#         av=l[i]
# print(mi,av,ma)

# n=int(input())
# ans=''
# s=input()
# if n==1:
#     print('YES')
# else:
#     for i in range(0,n-1):
#         s1=input()
#         if s[:s.find(' ')]<s1[:s.find(' ')]:
#             ans='YES'
#         elif s[:s.find(' ')]==s1[:s.find(' ')] and s[s.find('«'):]<s1[s.find('«'):]:
#             ans='YES'
#         else:
#             ans='NO'
#             break
#         s=s1
#     print(ans)

# s = 'Python rocks!'
# print(s.upper())

# s=input()
# s1=''
# for i in range(0,len(s)):
#     if i%3==0:
#         s1+=''
#     else:
#         s1+=s[i]
# print(s1)

# s=input()
# print(s.replace('1','one'))

# s=input()
# print(s.replace('@',''))

# s=input()
# if s.count('f')==1:
#     print(-1)
# elif s.count('f')==0:
#     print(-3)
# else:
#     s1=s[s.find('f')+1:]
#     print(s1.find('f')+len(s[:s.find('f')+1]))

# s=input()
# ind1=s.find('h')
# ind2=(s[::-1].find('h')+1)*(-1)
# print(s[:ind1+1]+s[ind1+1:ind2][::-1]+s[ind2:])

# n=int(input())
# l=[]
# for i in range(97,n+97):
#     l+=[chr(i)]
# print(l)


