# Задание 1

# n=int(input())
# n=str(n)
# print(int(n[::-1]))

# Задание 2
str_1=input()
str_2=input().lower()
print(str_2)
n,k=[],[]
n.extend(str_1)
k.extend(str_2)
k_low=[i.lower() for i in k]
for i in range(0,len(n)):
    if n[i].lower() in k_low:
        j=str_2.find(n[i].lower())
        print(f'{i+1} символ встречается в строке поиска:{str_2[:j]+str_2[j].upper()+str_2[j+1:]}')


