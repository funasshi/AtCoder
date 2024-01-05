N, K = map(int, input().split())
S = [input().rstrip() for _ in range(N)][:K]
S_sorted = sorted(S)
for i in range(K):
    print(S_sorted[i])
