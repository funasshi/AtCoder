n = int(input())
a = list(map(int, input().split()))


a1 = 0
for i in range(n):
    if i % 2 == 0:
        a1 += a[i]
    else:
        a1 -= a[i]
a1 //= 2

ans = [a1]

for i in range(n-1):
    ans.append(a[i]-ans[-1])

ans = [2*i for i in ans]
print(*ans)
