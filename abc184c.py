r1, c1 = [int(i) for i in input().split()]
r2, c2 = [int(i) for i in input().split()]


def jyouken(a, b, c, d):
    if a+b == c+d or a-b == c-d or abs(a-c)+abs(b-d) <= 3:
        return True
    return False


def jyouken2(a, b, c, d):
    if abs(a-c)+abs(b-d) <= 6:
        return True
    return False


def hani(a, b, c, d):
    check1 = d-c+a-b
    check2 = d+c-a-b

    if check1 % 2 == 0 or abs(check1) <= 3 or check2 % 2 == 0 or abs(check2) <= 3:
        return True
    return False


if r1 == r2 and c1 == c2:
    ans = 0
# 一手で行ける時
elif jyouken(r1, c1, r2, c2):
    ans = 1
    # 一手で行った先が範囲内の時
elif hani(r1, c1, r2, c2) or jyouken2(r1, c1, r2, c2):
    ans = 2
else:
    ans = 3

print(ans)
