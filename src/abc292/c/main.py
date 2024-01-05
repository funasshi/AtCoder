n = int(input())


def g(n):
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans += 1
    if int(n**0.5)**2 == n:
        ans += ans-1
    else:
        ans += ans
    return ans


ans = 0
for i in range(1, n):
    ans += g(i)*g(n-i)
print(ans)
