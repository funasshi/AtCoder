import numpy as np
n = int(input())
points = []
for _ in range(n):
    points.append(np.array([int(i) for i in input().split()]))


def tyokusen(a, b, c):
    x = a - b
    y = b - c
    if x[0] * y[1] == x[1] * y[0]:
        return True
    return False


flag = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = points[i]
            b = points[j]
            c = points[k]

            if tyokusen(a, b, c):
                flag = 1

if flag == 1:
    print('Yes')
else:
    print('No')
