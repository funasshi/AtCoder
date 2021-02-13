n, x = [int(i) for i in input().split()]
s = input()
point = x
for ox in s:
    if ox == 'o':
        point += 1
    else:
        point = max(0, point-1)
print(point)
