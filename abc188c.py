n = int(input())

a = [int(i) for i in input().split()]
k = len(a)

mae = a[:k//2]
usiro = a[k//2:]

point = min(max(mae), max(usiro))

for i in range(k):
    if a[i] == point:
        break

print(i+1)
