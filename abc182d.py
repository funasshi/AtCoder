n = int(input())
a = [int(i) for i in input().split()]


def get_jyunban_max():
    jyubnban_max = []
    now_max = 0
    now_sum = 0
    for i in a:
        now_sum += i
        if now_max < now_sum:
            now_max = now_sum
        jyubnban_max.append(now_max)
    return jyubnban_max


def get_dandan_tasiteku():
    dandan_tasiteku = []

    for i in range(n):
        if i == 0:
            dandan_tasiteku.append(a[0])
        else:
            dandan_tasiteku.append(a[i]+dandan_tasiteku[-1])
    return dandan_tasiteku


jyubnban_max = get_jyunban_max()
dandan_tasiteku = get_dandan_tasiteku()
sarani_dandan_tasiteku = []

now_max = 0
now_sum = 0
for i in range(n):
    now_max = now_sum+jyubnban_max[i]
    now_sum += dandan_tasiteku[i]
    sarani_dandan_tasiteku.append(now_max)

print(max(sarani_dandan_tasiteku))
