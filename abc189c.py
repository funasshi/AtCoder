n = int(input())

a = [int(i) for i in input().split()]

ans = 0
for i in range(n):
    min_num = a[i]
    for j in range(i, n):
        min_num = min(min_num, a[j])
        ans = max(min_num*(j-i+1), ans)
print(ans)
