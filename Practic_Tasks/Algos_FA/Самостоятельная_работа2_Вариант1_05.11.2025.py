import random
#2
A = set()
B = set()
while len(A)<5:
    A.add(random.randint(1,10))
while len(B)<5:
    B.add(random.randint(1,10))
print(A,B)
print(A-B)


#3
A = set()
while len(A)<5:
    A.add(random.randint(-10,10))

list_ = []
for item in list(A):
    if item>0:
        list_.append(item)

print(A)
print(list_)

#4
A = set()
B = set()
while len(A)<5:
    A.add(random.randint(1,10))
while len(B)<5:
    B.add(random.randint(1,10))

print(A,B)
print(A&B)