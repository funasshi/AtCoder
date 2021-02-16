a, b = map(int, input().split())

bitlen = len(format(b, 'b'))


def count(num, keta):
    ans = []
    for i in range(1, keta+1):
        cul = ((num+1)//(2**i))*(2**(i-1))
        cul += max(0, ((num+1) % (2**i))-(2**(i-1)))
        ans.append(cul)
    return ans


keta = len(format(b, 'b'))
ans1 = count(b, keta)
ans2 = count(a-1, keta)

ans = []
for i in range(keta):
    ans.append(str((ans1[i]-ans2[i]) % 2))
ans = ans[::-1]
print(int(''.join(ans), 2))
