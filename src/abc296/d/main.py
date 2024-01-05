import math

INF=10**30
# 入力
N, M = map(int, input().split())

# Xの最大の約数dを求める
kouho=INF
for a in range(1, math.ceil(M**0.5)+1):
    b=math.ceil(M/a)
    x=a*b
    if b<=N and a<=N:
        kouho=min(kouho,x)

if kouho==INF:
    print(-1)
else:
    print(kouho)