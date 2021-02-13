import queue


class Town:
    def __init__(self, name):
        self.name = name
        self.access_town = []
        self.step = 10 ** 9


n, m = [float(i) for i in input().split()]
towns = [None]+[Town(i + 1) for i in range(n)]

for _ in range(m):
    a, b, c = [float(i) for i in input().split()]
    towns[a].access_town.append([towns[b], c])

que = queue.Queue()


def sanpo(town, step):
    if town.step < step:
        return None
    town.step = step
    for i in town.access_town:
        que.put(i)


while not que.empty():
    sanpo(town)
