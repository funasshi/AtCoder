n, sober_limit = [int(i) for i in input().split()]
flag = 0
alcho_sum = 0
ans = -1
for _ in range(n):
    vol, percent = [int(i) for i in input().split()]

    alcho = vol * percent
    alcho_sum += alcho
    if alcho_sum > sober_limit*100 and flag == 0:
        flag = 1
        ans = _+1

print(ans)
