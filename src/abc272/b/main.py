n, m = map(int, input().split())

attendees = [[] for _ in range(n)]
for i in range(m):
    k, *x = map(int, input().split())
    for j in range(k):
        attendees[x[j]-1].append(i)

for i in range(n):
    for j in range(i+1, n):
        if len(set(attendees[i]) & set(attendees[j])) == 0:
            print("No")
            exit()
print("Yes")
