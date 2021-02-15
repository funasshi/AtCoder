s = input()
t = input()

n = len(s)
m = len(t)

sentou = -1


def func(s, t, i):
    if i+m > n:
        return False
    check = 0
    for j in range(i, i+m):
        if s[j] == t[j-i] or s[j] == "?":
            check += 1
    if check == m:
        return True
    return False


for i in range(n):
    if func(s, t, i):
        sentou = i

ans = []
if sentou == -1:
    print("UNRESTORABLE")
else:

    for i in range(n):
        if i > sentou and i <= sentou+m:
            ans.append(t[i-sentou])
        else:
            if s[i] == "?":
                ans.append("a")
            else:
                ans.append(s[i])
    print("".join(ans))
