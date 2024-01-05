import numpy as np
h, w = list(map(int, input().split()))
gyouretu = []
for i in range(h):
    gyouretu.append(list(map(int, input().split())))
gyouretu = np.array(gyouretu)
gyouretu = gyouretu.T

gyouretu = gyouretu.tolist()

for gyou in gyouretu:
    print(*gyou)
