n = int(input())
a = list(map(int, input().split()))

for i in range(1, n+1):
    a[i-1] -= i
a.sort()

ans = 0
for i in range(n//2):
    ans += a[-i-1]-a[i]

print(ans)
