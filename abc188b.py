import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
b = np.array([int(i) for i in input().split()])
Z = np.dot(a, b)

if Z == 0:
    print('Yes')
else:
    print('No')
