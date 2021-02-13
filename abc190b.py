n, time_limit, power_limit = [int(i) for i in input().split()]
flag = 0
for i in range(n):
    x, y = [int(i) for i in input().split()]
    if x >= time_limit or y <= power_limit:
        continue
    flag = 1

if flag == 1:
    print('Yes')
else:
    print('No')
