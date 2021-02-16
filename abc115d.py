n, x = map(int, input().split())


def get_next(n, i):
    if n == 0 and i == 0:
        return 1
    elif i == 0 or i == -1:
        return 0
    else:
        if i < 2**(n+1)-2:
            return get_next(n-1, i-1)
        else:
            return 2**(n+1)-1-get_next(n, 2**(n+2)-5-i)


ans = get_next(n, x-1)
print(ans)
