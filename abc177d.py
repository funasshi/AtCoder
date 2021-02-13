from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

n,m=[int(i) for i in input().split()]
data=[1]*m

row=[]
col=[]

for i in range(m):
    one,two=[int(i) for i in input().split()]
    n_one=min(one-1,two-1)
    n_two = max(one - 1, two - 1)
    row.append(n_one)
    col.append(n_two)

graph=csr_matrix((data,(row,col)),shape=(n,n))
num,label=connected_components(graph)

count_num=[0]*n
for i in label:
    count_num[i]+=1

print(max(count_num))

