# n=int(input())
# print('*'*19)
# for i in range(n-2):
#     print('*'+' '*17+'*')
# print('*'*19)



# n=int(input())
# z=n
# k=0
# while n!=0:
#     k+=1
#     n=n//10
# z=z//(10**(k-3))
# print(z%10)



# n = int(input())
# kol_3=0
# last_digit_counter=0
# ch_counter=0
# s_more_five = 0
# product_more_seven = 1
# zero_five_counter = 0
# last_digit = n%10
# while n!=0:
#     if n%10==3:
#         kol_3+=1
#     if n%10==last_digit:
#         last_digit_counter+=1
#     if n%10 in [0,2,4,6,8]:
#         ch_counter+=1
#     if n%10>5:
#         s_more_five+=n%10
#     if n%10>7:
#         product_more_seven*=n%10
#     if n%10==0 or n%10==5:
#         zero_five_counter+=1
#     n=n//10
# print(kol_3,last_digit_counter,ch_counter,s_more_five,product_more_seven,zero_five_counter,sep='\n')





for i in range(1,50):
    for j in range(1,50):
        q=i**3+j**3
        for z in range(1,50):
            for x in range(1,50):
                if z!=i and z!=j and x!=i and x!=j and q==z**3+x**3:
                    print(q)