import numpy as np
R = np.random.randint(0, 12, (3, 3))
print(R)
s = 0
try:
    if len(R) != len(R[0]):
        raise ValueError
    else:
        for i in range(len(R)):
            s+=R[i][i]
    print(s)
except ValueError:
    print("матрица не квадратная")