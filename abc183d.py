import numpy as np
n, w = [int(i) for i in input().split()]

timing = []
cost = []

for i in range(n):
    s, t, p = [int(i) for i in input().split()]
    timing += [s, t]
    cost += [p, -p]

timing = np.array(timing)
cost = np.array(cost)

arg_timing = np.argsort(timing)

timing = list(timing[arg_timing])
cost = list(cost[arg_timing])

height = 0
flag = 0
pre_timing = 0
for i in range(len(timing)):
    if height > w and pre_timing != timing[i]:
        flag = 1
    height += cost[i]
    pre_timing = timing[i]

if flag == 0:
    print('Yes')
else:
    print('No')
