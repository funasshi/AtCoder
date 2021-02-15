n, k = map(int, input().split())

mod = 10**9+7


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# modを考慮した組み合わせ
# nCrを高速に出力
# 上の２つが必要(egcd,modinv)
def combination(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res


for i in range(1, k+1):
    if i > n-k+1:
        print(0)
    else:
        print(combination(n-k+1, i, mod=mod) *
              combination(k-1, i-1, mod=mod) % mod)
