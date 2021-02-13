import queue
class Node:
    def __init__(self,name):
        self.name=name
        self.parent=None
        self.children=[]
        self.way=None

def set_route(caves):
    for _ in range(m):
        a,b=[int(i) for i in input().split()]
        caves[a].children.append(caves[b])
        caves[b].children.append(caves[a])

n,m=[int(i) for i in input().split()]
caves=["数合わせ"]+[Node(i) for i in range(1,n+1)]
set_route(caves)

q = queue.Queue()
caves[1].way=1
q.put(caves[1])

def set_way():
    cave=q.get()
    for next_cave in cave.children:
        if next_cave.way is not None:
            continue
        else:
            next_cave.way=cave.name
            q.put(next_cave)

while not q.empty():
    set_way()

print("Yes")
for i in caves[2:]:
    print(i.way)