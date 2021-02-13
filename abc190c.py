n, m = [int(i) for i in input().split()]
jyouken_list = []
for _ in range(m):
    jyouken_list.append([int(i) for i in input().split()])
irekata = []
k = int(input())

for _ in range(k):
    irekata.append([int(i) for i in input().split()])


def get_oku_pattern(i):
    return format(i, '0'+str(k)+'b')


def get_tama_pattern(oku_pattern):
    tama = [0]*n
    for i, ox in enumerate(oku_pattern):
        tama[irekata[i][int(ox)]-1] += 1
    return tama


def count_jyouken(oku_pattern):
    ans = 0
    tama_pattern = get_tama_pattern(oku_pattern)
    for jyouken in jyouken_list:
        one = jyouken[0]-1
        two = jyouken[1]-1
        if tama_pattern[one] != 0 and tama_pattern[two] != 0:
            ans += 1
    return ans


ans = 0
for i in range(2**k):
    oku_pattern = get_oku_pattern(i)
    ans = max(count_jyouken(oku_pattern), ans)

print(ans)
