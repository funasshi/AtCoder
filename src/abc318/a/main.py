# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)



n,m,p = list(map(int, input().split()))


s=n-m

if s<0:
    print(0)
else:
    print(1+s//p)

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
