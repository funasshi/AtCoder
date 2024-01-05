n = int(input())

retus = []


def cul_retu(n):
    ans = []
    i = n
    for j in range(n+1):
        if j == 0 or i == j:
            ans.append(1)
        else:
            ans.append(retus[i-1][j-1]+retus[i-1][j])
    return ans


for i in range(n):
    retus.append(cul_retu(i))

for retu in retus:
    print(*retu)
