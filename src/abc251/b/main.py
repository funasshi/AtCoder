import copy
n, w = list(map(int, input().split()))
a_list = list(map(int, input().split()))

# 一個選ぶものをすべて良い数に
good_n_list = copy.copy(a_list)

# 2個選ぶ

for i in range(n-1):
    for j in range(i+1, n):
        good_n_list.append(a_list[i]+a_list[j])

# 3個
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            good_n_list.append(a_list[i]+a_list[j]+a_list[k])

print(len([i for i in set(good_n_list) if i <= w]))
