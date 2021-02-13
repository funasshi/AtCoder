from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


class People:
    def __init__(self):
        self.frends = 0
        self.blocks = 0


n, m, k = [int(i) for i in input().split()]

data=[1]*m
row=[]
col=[]
peoples = [People() for i in range(n + 1)]
for i in range(m):
    one, two = [int(j) for j in input().split()]
    new_one=min(one,two)
    new_two=max(one,two)
    row.append(one)
    col.append(two)
    peoples[one].frends+=1
    peoples[two].frends+=1

frends = csr_matrix((data, (row, col)), shape=(n+1, n+1))


num, labels = connected_components(frends)
labels=list(labels)

for i in range(k):
    one, two = [int(j) for j in input().split()]
    if labels[one] == labels[two]:
        peoples[one].blocks+=1
        peoples[two].blocks+=1

renketu_num = [0]*num
for i in labels:
    renketu_num[i]+=1


def get_renketu_num(i):
    return renketu_num[labels[i]] - 1


def get_friend_num(i):
    return peoples[i].frends


def get_block_num(i):
    return peoples[i].blocks


for i in range(1, n + 1):
    print(get_renketu_num(i) - get_friend_num(i) - get_block_num(i))
