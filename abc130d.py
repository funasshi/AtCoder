n, k = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0

total = 0
ans = 0
for start in range(n):
    while total < k and end < n:
        total += a[end]
        end += 1
    if total >= k:
        ans += n-end+1
        total -= a[start]
    else:
        break
print(ans)
