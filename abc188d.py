import numpy as np
n, cb = [int(i) for i in input().split()]
time_list = []
cost_list = []
for _ in range(n):
    a, b, c = [int(i) for i in input().split()]
    time_list.append(a)
    time_list.append(b+1)
    cost_list.append(c)
    cost_list.append(-c)
time_list = np.array(time_list)
cost_list = np.array(cost_list)

time_arg = np.argsort(time_list)
time_list = list(time_list[time_arg])  # 価格が変動する時間
cost_list = list(cost_list[time_arg])

pre_time = -1
new_time_list = []
new_cost_list = []
for i in range(len(time_list)):
    if pre_time == time_list[i]:
        new_cost_list[-1] += cost_list[i]
    else:
        new_time_list.append(time_list[i])
        new_cost_list.append(cost_list[i])
        pre_time = time_list[i]

time_list = new_time_list
cost_list = new_cost_list

cost_sum = 0
now_day_cost = 0
pre_time = 0
#
for i in range(len(time_list)):
    time = time_list[i]
    cost = cost_list[i]
    cost_sum += min(now_day_cost, cb)*(time-pre_time)
    now_day_cost += cost
    pre_time = time

print(cost_sum)
