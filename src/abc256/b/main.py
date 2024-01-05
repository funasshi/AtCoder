n = int(input())
a_list = list(map(int, input().split()))

masu = []

p = 0
for a in a_list:
    masu.append(0)
    for i in range(len(masu)):
        masu[i] += a
    masu.sort()
    while True:
        if not masu:
            break
        tail = masu.pop()
        if tail >= 4:
            p += 1
        else:
            masu.append(tail)
            break


print(p)
