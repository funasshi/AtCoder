n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for a in range(1,n-2+1):
    for b in range(a,n-1+1):
        for c in range(b,n+1):
            if b in graph[a] and c in graph[b] and a in graph[c]:
                ans+=1
print(ans)
