h, w = [int(i) for i in input().split()]
masu = [list(input()) for i in range(h)]
mod = 10**9+7
ans_masu = [[0]*w for i in range(h)]

k = 0
for i in masu:
    for j in i:
        if j == ".":
            k += 1


def retu(index):
    pre = "#"
    start = -1
    end = -1
    count = 0
    for i in range(h):
        if masu[i][index] == "#":
            if pre == ".":
                pre = "#"
                end = i
                for j in range(start, end):
                    ans_masu[j][index] = count
            count = 0
            pre = "#"
        else:
            start = i
            count += 1
            pre = "."


def gyou(index):
    pre = "#"
    start = -1
    end = -1
    count = 0
    for i in range(w):
        if masu[index][i] == "#":
            if pre == ".":
                pre = "#"
                end = i
                for j in range(start, end):
                    ans_masu[index][j] = +count
            count = 0
            pre = "#"
        else:
            start = i
            count += 1
            pre = "."


for i in range(h):
    gyou(i)
for j in range(w):
    retu(j)


def power(k):
    ans = 1
    for i in range(k):
        ans *= 2
        ans = ans % mod
    return ans


def get(n):
    return power(k)-power(k-n)


ans = 0
for masu in ans_masu:
    for i in masu:
        ans += get(i)
        ans = ans % mod

print(ans)
