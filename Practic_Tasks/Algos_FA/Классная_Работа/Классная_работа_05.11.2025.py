# 1
# numbers = {
#     'пятьдесят':50,
#     'шестьдесят':60,
#     'пять':5,
#     'шесть':6,
# }

# numbers_int={}
# for k,v in numbers.items():
#     numbers_int[v]=k

# # print(numbers_int)

# var = int(input())
# sum=[]
# if var>9:
#     sum.append(str(numbers_int[var//10*10]))
# sum.append(str(numbers_int[var%10]))
# print(' '.join(sum))


# 2
# letters = ["T", "O", "L", "I", "K"]
# chars = ["-.", ".-", "..", ".-.", "..-"]
# d = {}
# for i in range(len(letters)):
#     d[chars[i]] = letters[i]

# d_in={}
# for i in range(len(letters)):
#     d_in[letters[i]] = chars[i]


# def from_morze(a):
#     words=[]
#     words = a.split('   ')
#     morze = []
#     for i in words:
#         i = i.split(' ')
#         morze.append(i)
#         print(i)

#     for i in morze:
#         for j in range(len(i)):
#             i[j]=d[i[j]]

#     for i in range(len(morze)):
#         morze[i]=''.join(morze[i])

#     print(*morze,sep = ' ')


# def in_morze(b):
#     words=[]
#     words = b.split('   ')
#     morze = []
#     for i in words:
#         i = i.split(' ')
#         morze.append(i)
#         print(i)

#     for i in morze:
#         for j in range(len(i)):
#             i[j]=d_in[i[j]]

#     for i in range(len(morze)):
#         morze[i]=' '.join(morze[i])
#     print(*morze,sep = ' ')

# in_morze(input())


# 7
# d = [(i,i**2) for i in range(1,16)]
# d_1 = {}
# d_1.update(d)
# print(d_1)


# 8
# d = {1: "q", 2: "w"}
# d_1 = {3:'e',4:'r'}
# d.update(d_1)
# print(d)


# 9
# dict = {1: "q", 2: "w", 3: "e", 4: "r", 5: "t"}
# for k,v in dict.items():
#     print(k, ' = ', v)

# 10
# dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}
# sum=0
# for v in dict.values():
#     sum+=v

# print(sum)


# 11
# dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}
# product = 1
# for v in dict.values():
#     product *= v

# print(product)



#12
# key = int(input())
# dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}
# del dict[key]
# print(dict)


#13
# list_1 = [1,2,3,4,5]
# list_2 = [1,2,3,4,5]
# list_con = [(list_1[i],list_2[i]) for i in range(len(list_1))]
# d = {}
# d.update(list_con)
# print(d)



#22
# dict_ = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict = dict_.copy()
# a = int(input())
# for k,v in dict.items():
#     if dict_[k]<a:
#         del dict_[k]

# print(dict_)

#23
# dict_ = {1: '1', 2: '11', 3: '111', 4: '1111', 5: '11111'}
# max_key = None
# max_value = -100000000000000000000
# for k,v in dict_.items():
#     if len(v)>max_value:
#         max_key = k

# print(max_key)



#24
# dict_ = {1: '1', 2: '11', 10: '111', 4: '1111', 5: '11111'}

# dict_1 = {}

# list_ = [(k,v) for k,v in dict_.items()]
# list_ = list_[::-1]
# dict_1.update(list_)
# print(dict_1)



# dict_2 = dict(sorted(dict_.items(), reverse=True))
# print(dict_2)


#25
# letter = input()
# dict_ = {'1': '1', '2': '11', '10': '111', '4': '1111', '5': '11111'}
# dict_1 = dict_.copy()
# for k in dict_.keys():
#     if k[0]==letter:
#         del dict_1[k]

# print(dict_1)


#1
# q = [(1,'2'),(2,'2')]
# d = {}
# d.update(q)
# print(d)

#1
import random
# A = set()
# B = set()
# while len(A)<10:
#     A.add(random.randint(1,10))
# while len(B)<5:
#     B.add(random.randint(1,10))
# print(A,B)
# print(A|B)
# print(A&B)
# print(A-B)
# print(A^B)
# print(A.issubset(B))
# print(B.issubset(A))


#2
# t1 = set(['Иванов','Петров','Сидоров','Хохлов','Гуров'])
# t2 = set(['Иванов','Антипов','Горохов','Хохлов','Гуров'])
# t3 = set(['Фокина','Антипов','Шкель','Хохлов','Шаронов'])
# print(t1|t2|t3, 'Решил хотя бф 1 задачу')
# print(t1&t2&t3, 'Решил все задачи')
# print((t1|t2|t3)-(t1&t2&t3)-(t1&t2)-(t1&t3)-(t2&t3), 'ровно 1 задачу')
# print((t1|t2|t3)-(t1&t2&t3)-(t1&t2)-(t1-(t1&t3))-(t2-(t2&t3))-(t2-(t2&t1)), 'ровно 2 задачу')
