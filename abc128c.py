

n, m = map(int, input().split())


hituyou_switch = []
for i in range(m):
    k, *s = map(int, input().split())
    hituyou_switch.append(s)
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    # パターンごとに計算
    switch_pattern = format(i, '0'+str(n+1)+'b')
    count = 0

    # 全ての電球について考える
    for j, denkyu_switch_num in enumerate(hituyou_switch):
        on = 0
        for switch_num in denkyu_switch_num:
            if switch_pattern[switch_num] == '1':
                on += 1
        if on % 2 == p[j]:
            count += 1

    if count == m:
        ans += 1
print(ans)
