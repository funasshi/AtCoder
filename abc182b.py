# 1000以下の素数を列挙
import math
prime_number = []


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


for i in range(2, 1000):
    if is_prime(i):
        prime_number.append(i)

n = int(input())

a = [int(i) for i in input().split()]


def gcd(k):
    ans = 0
    for i in a:
        if i % k == 0:
            ans += 1
    return ans


max_gcd = 0
ans = 0
for k in prime_number:
    if max_gcd < gcd(k):
        ans = k
        max_gcd = gcd(k)

print(ans)
