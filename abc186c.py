def not7with10(n):
    n_list = list(str(n))
    if '7' in n_list:
        return False
    return True


def not7with8(n):
    n_list = list(oct(n))
    if '7' in n_list:
        return False
    return True


n = int(input())

ans = 0
for i in range(1, n+1):
    if not7with10(i) and not7with8(i):
        ans += 1

print(ans)
