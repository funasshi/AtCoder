n = int(input())


def pysum(k):
    return k*(k+1)//2


ans = 0
for i in range(n):
    a, b = [int(i) for i in input().split()]
    ans += pysum(b) - pysum(a - 1)
print(ans)
