from collections import defaultdict

# 入力を受け取る
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 隣接リストを作成する
adj_list = defaultdict(list)
for a, b in edges:
    adj_list[a].append(b)
    adj_list[b].append(a)

# 隣接リストを出力する
for i in range(1, n + 1):
    adj = sorted(adj_list[i])
    print(len(adj), *adj)
