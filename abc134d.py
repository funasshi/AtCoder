import math
n = int(input())
a = [0]+list(map(int, input().split()))
ans = [0]*(n+1)

for i in range(n, 0, -1):
    if i > n/2:
        ans[i] = a[i]
    else:
        for j in range(2*i, n+1, i):
            ans[i] += ans[j]
        ans[i] %= 2
        if ans[i] != a[i]:
            ans[i] = 1
        else:
            ans[i] = 0
print(sum(ans))
for i in range(n+1):
    if ans[i] == 1:
        print(i, end=' ')
if sum(ans) != 0:
    print('')
