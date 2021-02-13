import numpy as np
h, w = [int(i) for i in input().split()]
a = []
for _ in range(h):
    a += [int(i) for i in input().split()]
a = np.array(a)
min_a = np.min(a)
a = a - min_a
print(sum(a))
