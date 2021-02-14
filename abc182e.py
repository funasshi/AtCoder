h, w, n, m = [int(i) for i in input().split()]


jyoutai = [[0]*w for i in range(h)]

# 電球を入れる
for _ in range(n):
    a, b = [int(i)-1 for i in input().split()]
    jyoutai[a][b] = 1

# ブロックを入れる
for _ in range(m):
    a, b = [int(i)-1 for i in input().split()]
    jyoutai[a][b] = -1

# 左向きに調べる
# 答えを書き込むリスト


def light_count(jyoutai):
    h = len(jyoutai)
    w = len(jyoutai[0])
    hyou = [[0]*w for i in range(h)]
    for i, row in enumerate(jyoutai):
        for j, object in enumerate(row):
            if j == 0:
                if object == 1:
                    hyou[i][j] = 1
            else:
                if object == 1:
                    hyou[i][j] = 1
                elif object == -1:
                    hyou[i][j] = 0
                else:
                    hyou[i][j] = hyou[i][j-1]
    return hyou


def make_tenti(list_sample):
    h = len(list_sample)
    w = len(list_sample[0])
    ans = [[0]*h for i in range(w)]
    for i in range(h):
        for j in range(w):
            ans[j][i] = list_sample[i][j]
    return ans


def make_flip(list_sample):
    h = len(list_sample)
    w = len(list_sample[0])
    ans = [[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            ans[i][w-j-1] = list_sample[i][j]
    return ans


ans1 = light_count(jyoutai)
ans2 = make_tenti(light_count(make_tenti(jyoutai)))
ans3 = make_flip(light_count(make_flip(jyoutai)))
ans4 = make_tenti(make_flip(light_count(make_flip(make_tenti(jyoutai)))))
answer = 0
for i in range(h):
    for j in range(w):
        if ans1[i][j] == 1 or ans2[i][j] == 1 or ans3[i][j] == 1 or ans4[i][j] == 1:
            answer += 1
print(answer)
