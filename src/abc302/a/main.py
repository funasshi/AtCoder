# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


a, b = list(map(int, input().split()))

shou=a//b


if a-b*shou>0:
    print(shou+1)
else:
    print(shou)

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
