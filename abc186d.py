n = int(input())
a = [int(i) for i in input().split()]
a.sort()


ans = 0
pre_sum = 0
for i in a:
    ans += i-a[0]
    pre_sum = ans

for i in range(1, n):
    pre_sum = pre_sum-(a[i]-a[i-1])*(n-i)
    ans += pre_sum

print(ans)
