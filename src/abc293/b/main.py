n = int(input())
a = list(map(int, input().split()))

called = [False] * n
for i in range(n):
    a[i] -= 1  # 0-indexedに変換
    if not called[i]:
        called[a[i]] = True

not_called = [i+1 for i in range(n) if not called[i]]
k = len(not_called)
print(k)
print(*not_called)
