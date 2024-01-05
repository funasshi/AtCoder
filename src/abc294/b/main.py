H, W = map(int, input().split())

A = []
for i in range(H):
    A.append(list(map(int, input().split())))

for i in range(H):
    S = ""
    for j in range(W):
        if A[i][j] == 0:
            S += "."
        else:
            S += chr(ord("A") + A[i][j] - 1)
    print(S)
