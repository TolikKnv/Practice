# s = 'wdcw wfcwef   wfwf   wfww22f    wfw3fg3'
# s1=s.split()
# s=''
# for i in range(len(s1)):
#     s+=s1[i]+' '
# print(s)

s='Awdwf wqfw qfwfw'
k=0
for i in range(0,3):
    if s[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        k+=1
if k>1:
    print(s.upper())
else:
    print(s)

# s='0123456789'
# print(s[::2])
