eight_jyoukens = []

for i in range(0, 1000, 8):
    eight_jyouken = [0]*10
    for num in format(i, "03d"):
        eight_jyouken[int(num)] += 1
    eight_jyoukens.append(eight_jyouken)


def check(jyouken):
    for i in range(10):
        if jyouken[i] > num_list[i]:
            return False
    return True


taishou = int(input())

if taishou in list(range(0, 100, 8))+[61, 42, 23, 84, 65, 46, 27, 69]:
    print('Yes')
elif taishou < 100:
    print('No')
else:
    num_list = [0]*10

    for num in str(taishou):
        num_list[int(num)] += 1

    flag = 0
    for jyouken in eight_jyoukens:
        if check(jyouken):
            flag = 1
            break

    if flag == 1:
        print('Yes')
    else:
        print('No')
