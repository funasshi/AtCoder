# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)

n=int(input())
s=input()

b=list(s)
ans=''
for i in b:
    ans+=i+i
    
print(ans)

# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
