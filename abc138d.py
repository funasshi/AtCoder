import sys
sys.setrecursionlimit(10**6)


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.count = 0
        self.visited = False


n, q = map(int, input().split())

nodes = [None]

for i in range(1, n+1):
    nodes.append(Node(i))

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].children.append(nodes[b])
    nodes[b].children.append(nodes[a])


for _ in range(q):
    p, x = map(int, input().split())
    nodes[p].count += x


q = []
q.append(nodes[1])
while q:
    node = q.pop()
    node.visited = True
    for child in node.children:
        if not child.visited:
            child.count += node.count
            q.append(child)

for i in nodes:
    if i is not None:
        print(i.count, end=' ')

print('')
