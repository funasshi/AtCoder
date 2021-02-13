n = int(input())
a = [int(i) for i in input().split()]

j_Aj = [0]

for j, aj in enumerate(a):
    j_Aj.append(j + 1 - aj)
maxj=max(j_Aj)
i_Ai = [0] * (maxj+1)
ans = 0
for j, j_aj in enumerate(j_Aj):
    if j == 0:
        continue
    if j_aj >= 2:
        ans += i_Ai[j_aj]
    if j + a[j - 1]<=maxj:
        i_Ai[j + a[j - 1]] += 1
print(ans)
