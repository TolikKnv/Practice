l = [1,3,231,34,23,213,11,34,2131,12]


def sum_odd(list):
    if len(list)==0:
        return 0
    if list[0] % 2==1:
        return sum_odd(list[1:]) + list[0]
    else:
        return sum_odd(list[1:])
print(sum_odd(l))