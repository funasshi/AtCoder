MOD = 998244353

A, B, C, D, E, F = map(int, input().split())

A=A%MOD
B=B%MOD
C=C%MOD
D=D%MOD
E=E%MOD
F=F%MOD

abc = (A * B * C )% MOD
def_ = (D * E * F) % MOD

print((abc - def_) % MOD)