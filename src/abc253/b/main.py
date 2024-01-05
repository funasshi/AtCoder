h, w = list(map(int, input().split()))
masu = []

for i in range(h):
    s = input()

    ans = [j for j, x in enumerate(s) if x == "o"]
    for j in ans:
        masu.append([i, j])

one = masu[0]
two = masu[1]

print(abs(one[0]-two[0])+abs(one[1]-two[1]))
