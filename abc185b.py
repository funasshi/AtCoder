n, m, t = [int(i) for i in input().split()]
battery = n
out = 0
flag = 1
for _ in range(m):
    a, b = [int(i) for i in input().split()]
    n = n - (a - out)
    if n <= 0:
        flag = 0
        break
    else:
        n += (b - a)
        n = min(n, battery)
        out = b

if flag == 0:
    print('No')

else:
    if n > t - out:
        print('Yes')
    else:
        print('No')
