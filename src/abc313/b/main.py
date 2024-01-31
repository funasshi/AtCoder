# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n,m= list(map(int, input().split()))


class Programmer:
    def __init__(self,name,weakers,strongers) -> None:
        self.name=name
        self.weakers=weakers
        self.strongers=strongers
programmers=[None]+[Programmer(i+1,[],[]) for i in range(n)]

def add_weaker(stronger,weaker):
    if weaker.name in stronger.weakers:
        pass
    else:
        stronger.weakers.append(weaker.name)
    if stronger.name
    for very_weaker_id in weaker.weakers:
        very_weaker=programmers[very_weaker_id]
        add_weaker(stronger,very_weaker)
for i in range(m):
    stronger,weaker = list(map(int, input().split()))
    add_weaker(programmers[stronger],programmers[weaker])

strongest=-1

for i in range(1,n+1):
    programmer=programmers[i]
    if len(set(programmer.weakers))==n-1:
        strongest=i

print(strongest)

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
