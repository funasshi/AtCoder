n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

ans = []

for i in a:
    if i != x:
        ans.append(str(i))

print(" ".join(ans))
