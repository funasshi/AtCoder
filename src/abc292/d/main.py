from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
n, m = list(map(int, input().split()))


row = []
col = []

for i in range(m):
    u, v = list(map(int, input().split()))
    row.append(u-1)
    col.append(v-1)

data = [1]*len(row)

matrix = csr_matrix((data, (row, col)), (n, n))

renketu_num, labels = connected_components(matrix)

hen = [0]*renketu_num
tyouten = [0]*renketu_num


for i in range(m):
    hen[labels[row[i]]] += 1
for t in labels:
    tyouten[t] += 1


def hen_number(i):
    try:
        return hen[i]
    except e:
        return -1


def tyouten_number(i):
    try:
        return tyouten[i]
    except e:
        return -5


# 各連結成分について調べる
flag = 0
for i in range(renketu_num):
    if hen_number(i) != tyouten_number(i):
        flag = 1

if flag == 1:
    print("No")
else:
    print("Yes")
