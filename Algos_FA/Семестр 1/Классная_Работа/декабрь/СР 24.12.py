# 1
# def prod(*args):
#     rez = 1
#     try:
#         for i in args:
#             if isinstance(i, int):
#                 rez*=i
#             else:
#                 raise ValueError
#         print(rez)
#     except ValueError:
#         print('ValueError')

# prod(1,2,3,4,2,423,34,'123', 123)


# 2
def prod(a, b=1, c=1):
    rez = 1
    rez = rez * a * b * c
    print(rez)


l = [2,3,4]
for i in range(1,4):
    prod(*l[:i])


#3
# a = [1,2,3,4,5]
# rez = [a[i]*i for i in range(len(a))]
# print(rez)


#4
# with open(r'C:\Users\Honor\Desktop\СР24.12.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()
#     el = list(set(text.split()))

# with open('new.txt', 'w', encoding='UTF-8') as f:
#     for i in el:
#         col = text.count(i)
#         f.write(f'{i} в тексте: {col} \n')

