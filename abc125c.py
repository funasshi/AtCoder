import math

n = int(input())
a = list(map(int, input().split()))
front = [a[-1], a[0]]
back = [a[0], a[-1]]

for i in range(1, n-1):
    front.append(math.gcd(front[-1], a[i]))
for i in range(n-2, 0, -1):
    back.append(math.gcd(back[-1], a[i]))

back = back[::-1]
max_gcd = 1
for i in range(n):
    max_gcd = max(max_gcd, math.gcd(front[i], back[i]))

print(max_gcd)
