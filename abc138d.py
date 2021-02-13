class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.count = 0


n, q = [int(i) for i in input().split()]

nodes = [None]+[Node(i) for i in range(1, n+1)]

for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    nodes[a].children.append(nodes[b])
    nodes[b].children.append(nodes[a])

# 親をつける


def make_oya(node):
    for child in node.children:
        child.parent = node
        child.children.remove(node)
        make_oya(child)


make_oya(nodes[1])

for _ in range(q):
    p, x = [int(i) for i in input().split()]
    nodes[p].count += x


def cul_count(node):
    for child in node.children:
        cul_count(child)
