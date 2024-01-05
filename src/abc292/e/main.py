import sys
n, m = list(map(int, input().split()))
sys.setrecursionlimit(10**9)
jisho = {}


class Node:
    def __init__(self, number):
        self.number = number
        self.children = []
        self.parents = []


nodes = [None]
for i in range(n):
    nodes.append(Node(i+1))

row = []
col = []

for i in range(m):
    u, v = list(map(int, input().split()))
    row.append(u)
    col.append(v)
    nodes[u].children.append(nodes[v])
    nodes[v].parents.append(nodes[u])


def check_back(two, three):
    ans = 0
    for one in two.parents:
        if three not in one.children and three.number != one.number:
            ans += 1
            one.children.append(three)
            three.parents.append(one)
            ans += check_front(one, three)
            ans += check_back(one, three)
    return ans


def check_front(one, two):
    ans = 0
    threes = two.children
    for three in threes:
        if three not in one.children and three.number != one.number:
            ans += 1
            one.children.append(three)
            three.parents.append(one)
            ans += check_front(one, three)
            ans += check_back(one, three)
    return ans


ans = 0
for i in range(m):
    one = nodes[row[i]]
    two = nodes[col[i]]
    ans += check_front(one, two)

print(ans)
