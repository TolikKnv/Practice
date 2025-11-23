#1
# a = map(int,input().split())
# print(sum(a))

#2
# with open("input.txt", "r") as f:
#     a, b = map(int, f.read().split())

# with open("output.txt", "w") as f:
#     f.write(str(a + b))


#6
j = input()
s = input()
k = 0
for item in s:
    if item in j:
        k+=1
print(k)
