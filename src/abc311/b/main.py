# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n,d=list(map(int, input().split()))
s_list=[]
for i in range(n):
    s_list.append(input())

ans=""
for i in range(d):
    a=set()
    for j in range(n):
        a.add(s_list[j][i])
    if list(a)==['o']:
        ans+='o'
    else:
        ans+='x'

renzoku=0
max_renzoku=0
for i in range(d):
    if ans[i]=='o':
        renzoku+=1
        max_renzoku=max(max_renzoku,renzoku)
    else:
        renzoku=0

print(max_renzoku)
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
