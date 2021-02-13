x, y = [int(i) for i in input().split()]
X = min(x, y)
Y = max(x, y)

if Y - X <= 2:
    print('Yes')
else:
    print('No')
