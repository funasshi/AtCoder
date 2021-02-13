n = int(input())

ans = 0


def is_able_to_split(i):
    hituyou = i*(i+1)//2
    if hituyou <= n:
        return True
    return False


for i in range(1, int(2*n**0.5)+1):
    if not is_able_to_split(i):
        break
    elif i % 2 == 0:  # 偶数の時
        if n % i == i//2:
            ans += 1
    else:
        if n % i == 0:
            ans += 1
print(2*ans)
