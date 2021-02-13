n = int(input())
a = [int(i) for i in input().split()]

ball_count = [0] * (n + 1)

for i in a:
    ball_count[i] += 1
def nCr(i):
    if i<=1:
        return 0
    else:
        return i*(i-1)//2

def get_total(ball_count):
    ans = 0
    for i in ball_count:
        ans += nCr(i)
    return ans


total = get_total(ball_count)
for i in range(1, n + 1):
    num = ball_count[a[i - 1]]
    ans = total - nCr(num) + nCr(num-1)
    print(ans)
