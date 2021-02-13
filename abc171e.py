n = int(input())
a = [int(i) for i in input().split()]

# まずは１を特定
one = 0
for i in a[1:]:
    one = one ^ i

ans = [str(one)]

for i in a[1:]:
    ans.append(str(one ^ a[0] ^ i))

print(' '.join(ans))
