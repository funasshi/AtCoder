class Node(object):
    def __init__(self, name, price):
        self.name = name
        self.children = []
        self.price = price
        self.most_ureru_price = None


n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

nodes = [None]+[Node(i+1, price) for i, price in enumerate(a)]

for i in range(m):
    x, y = [int(i) for i in input().split()]
    nodes[x].children.append(nodes[y])


def get_most_ureru_price(node):
    children = node.children
    if len(children) != 0:
        node.most_ureru_price = 0
        for child in children:
            node.most_ureru_price = max(
                node.most_ureru_price, child.price)
            if child.most_ureru_price is not None:
                node.most_ureru_price = max(
                    node.most_ureru_price, child.most_ureru_price)


for i in range(n, 0, -1):
    node = nodes[i]
    get_most_ureru_price(node)

ans = -10**9
for node in nodes:
    if node is not None:
        if node.most_ureru_price is not None:
            ans = max(ans, node.most_ureru_price-node.price)

print(ans)
