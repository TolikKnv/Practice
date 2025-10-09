# s=input()
# s=s.split()
# for i in s:
#     print(s[i])

# s=input()
# s=s.split()
# for i in range (len(s)):
#     s[i]=s[i][0]
# print('.'.join(s))

# s=input()
# s=s.split('.')
# otv=''
# for i in s:
#     if 0<=int(i)<=255:
#         otv='ДА'
#     else:
#         otv='НЕТ'
#         break
# print(otv)

s=input()
s=s.split()
k=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            k+=1
print(k)
