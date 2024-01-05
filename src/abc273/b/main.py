X, K = map(int, input().split())

for i in range(K):
    if X % (10 ** (i+1)) >= 5 * (10 ** i):
        X = (X // (10 ** (i+1))) * (10 ** (i+1)) + (10 ** (i+1))
    else:
        X = (X // (10 ** (i+1))) * (10 ** (i+1))

print(X)
