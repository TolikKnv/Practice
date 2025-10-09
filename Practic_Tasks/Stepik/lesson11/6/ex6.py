# num = [8, 9, 10, 11]
# num[1]=17
# num+=[4,5,6]
# num.pop(0)
# num=num*2
# num.insert(3,25)
# print(num)

# s=input()
# s=s.lower()
# s=s.split()
# print(f'Общее количество артиклей: {s.count('the')+s.count('an')+s.count('a')}')

# s=input()
# s=s.split()
# for i in range(0,len(s)):
#     s[i]=int(s[i])
# ma=max(s)
# mi=min(s)
# indma=s.index(ma)
# indmi=s.index(mi)
# s[indma]=mi
# s[indmi]=ma
# print(*s)

# s=input()
# s=int(s[1:])
# output=''
# for i in range(s):
#     d=input()
#     if '#' not in d:
#         output+=d.rstrip()+'\n'
#     else:
#         d=d.split('#')
#         d=d[0].rstrip()
#         output+=d+'\n'
# print(output)

# s=input()
# s=s.split()
# l=[]
# for i in range (len(s)):
#     l+=[int(s[i])]
# l.sort()
# print(*l)
# l.sort(reverse=True)
# print(*l)

n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
l.sort()
for i in range(len(l)):
    print(l[i])
