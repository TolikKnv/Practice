# n = int(input())
# num = [i for i in range(2,n+1,2)]
# print(num)


# str1=input()
# str2=input()
# l=[int(i) for i in str1.split()]
# m=[int(i) for i in str2.split()]
# otv=[l[i]+m[i] for i in range(0,len(l))]
# print(*otv)



# str1 = input()
# num = [int(i) for i in str1.split()]
# print(*num,sep='+',end='=')
# print(sum(num))


# s=input()
# if s.count('-')==2 or s.count('-')==3:
#     s=s.split('-')
#     if (len(s)==4 and len(s[0])==1 and len(s[1])==3 and len(s[2])==3 and len(s[3])==4) or (len(s)==3 and len(s[0])==3 and len(s[1])==3 and len(s[2])==4):
#         s=''.join(s)
#         if len(s)==10 and all(x in '0123456789' for x in s):
#             print('YES')
#         elif len(s)==11 and s[0]=='7' and all(x in '0123456789' for x in s):
#             print('YES')
#         else:
#             print('NO')
#     else:
#         print('NO')
# else:
#     print('NO')




# s = input()
# l = [i[1:]+i[1]+'ки' for i in s.split()]
# print(*l)

