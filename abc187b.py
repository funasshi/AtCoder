n = int(input())
points = []
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    points.append((x, y))
ans = 0


def check(xa, ya, xb, yb):
    if xa == xb:
        return False
    if abs((yb - ya) / (xb - xa)) <= 1:
        return True
    return False


for i in range(n):
    for j in range(i + 1, n):
        xa, ya = points[i]
        xb, yb = points[j]
        if check(xa, ya, xb, yb):
            ans += 1

print(ans)
