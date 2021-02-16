def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n, m = map(int, input().split())
limit = m//n
for i in make_divisors(m)[::-1]:
    if limit < i:
        pass
    else:
        break
print(i)
