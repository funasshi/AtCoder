s = input()
t = input()

n = len(s)
m = len(t)


def check(sentou):
    for i in range(m):
        if s[sentou+i] != t[i] and s[sentou+i] != '?':
            return False
    return True


def make(sentou):
    ans = list(s)
    for i in range(m):
        ans[sentou+i] = t[i]
    for i in range(n):
        if ans[i] == '?':
            ans[i] = 'a'
    return ''.join(ans)


ans_list = []
for sentou in range(n-m+1):
    if check(sentou):
        ans_list.append(make(sentou))

ans_list.sort()
if len(ans_list) == 0:
    print('UNRESTORABLE')
else:
    print(ans_list[0])
