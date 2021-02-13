h, w = [int(i) for i in input().split()]

masu = []
for _ in range(h):
    masu.append(list(input()))


def get_black_kado(i, j):
    top = masu[i - 1][j]
    bottom = masu[i + 1][j]
    left = masu[i][j-1]
    right = masu[i][j + 1]
    white_num = 0
    black_num = 0
    for bw in [top, bottom, left, right]:
        if bw == '.':
            white_num += 1
        else:
            black_num += 1
    if white_num == 4:
        totu = 4
    elif white_num == 3:
        totu = 2
    elif white_num == 2:
        if (top == '.' and bottom == '.') or (left == '.' and right == '.'):
            totu = 0
        else:
            totu = 1
    else:
        totu = 0
    return totu


def get_white_kado(i, j):
    top = masu[i - 1][j]
    bottom = masu[i + 1][j]
    left = masu[i][j-1]
    right = masu[i][j + 1]
    white_num = 0
    black_num = 0
    for bw in [top, bottom, left, right]:
        if bw == '.':
            white_num += 1
        else:
            black_num += 1
    if black_num == 4:
        totu = 4
    elif black_num == 3:
        totu = 2
    elif black_num == 2:
        if (top == '.' and bottom == '.') or (left == '.' and right == '.'):
            totu = 0
        else:
            totu = 1
    else:
        totu = 0
    return totu


totu = 0
ou = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if masu[i][j] == '#':
            totu += get_black_kado(i, j)
        else:
            ou += get_white_kado(i, j)
print(totu+ou)
