x = input().strip()
n = int(input())
s = [input().strip() for i in range(n)]

# 辞書順での大小関係を定義
order = {c: i for i, c in enumerate(x)}

# 辞書順に従って s をソート
s.sort(key=lambda w: [order[c] for c in w])

# ソートした s を出力
for w in s:
    print(w)
