n, k, q = list(map(int, input().split()))
koma_place_list = list(map(int, input().split()))
l_list = list(map(int, input().split()))

masu_list = [0]*(n+1)

for a in koma_place_list:
    masu_list[a] = 1


def move(l):
    masu_list[koma_place_list[l-1]] = 0
    masu_list[koma_place_list[l-1]+1] = 1
    koma_place_list[l-1] += 1


def sousa(l):
    masu = koma_place_list[l-1]
    if masu == n:
        return
    next_koma = masu+1
    if masu_list[next_koma] == 0:
        move(l)


for l in l_list:
    sousa(l)

ans = []
for i, m in enumerate(masu_list):
    if m:
        ans.append(i)


print(*ans)
