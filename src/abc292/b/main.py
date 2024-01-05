n, q = list(map(int, input().split()))
events = []
for i in range(q):
    events.append(list(map(int, input().split())))

points = [0]*(n+1)

for event in events:
    i, x = event
    if i == 1:
        points[x] += 1
    elif i == 2:
        points[x] += 2
    else:
        if points[x] >= 2:
            print("Yes")
        else:
            print("No")
