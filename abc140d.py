n, k = map(int, input().split())
s = input()

LR = 0
RL = 0

for i in range(1, n):
    if s[i-1]+s[i] == 'LR':
        LR += 1
    elif s[i-1]+s[i] == 'RL':
        RL += 1

moto = 0
for i in range(1, n):
    if s[i-1]+s[i] == 'LL':
        moto += 1
    elif s[i-1]+s[i] == 'RR':
        moto += 1

# ひっくり返してプラス２できる回数
two = min(LR, RL)


if two >= k:
    print(k*2+moto)
else:
    print(n-1)
