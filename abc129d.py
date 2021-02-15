h, w = [int(i) for i in input().split()]
masu = []
for i in range(h):
    masu.append(list(input()))


def light_count(masu):
    h = len(masu)
    w = len(masu[0])

    count_map = [[0]*w for i in range(h)]
    for i, retu in enumerate(masu):
        for j, item in enumerate(retu):
            if j == 0:
                if item == '.':
                    count_map[i][j] = 1
            elif item == '.':
                count_map[i][j] = count_map[i][j-1]+1
        for j in range(w-1, -1, -1):
            if j == w-1 or count_map[i][j] == 0:
                continue
            else:
                if count_map[i][j+1] == 0:
                    continue
                else:
                    count_map[i][j] = count_map[i][j+1]
    return count_map


def make_tenti(list_sample):
    h = len(list_sample)
    w = len(list_sample[0])
    ans = [[0]*h for i in range(w)]
    for i in range(h):
        for j in range(w):
            ans[j][i] = list_sample[i][j]
    return ans


ans1 = light_count(masu)
ans2 = make_tenti(light_count(make_tenti(masu)))

ans = [0]

for i in range(h):
    for j in range(w):
        if ans1[i][j]+ans2[i][j] != 0:
            ans.append(ans1[i][j]+ans2[i][j]-1)

print(max(ans))
