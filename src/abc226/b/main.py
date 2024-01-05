n = int(input())
b = []
for i in range(n):
    b.append("_".join(input().split()))
print(len(list(set(b))))
