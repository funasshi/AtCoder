# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


s=list(input())

print(''.join([i for i in s if i not in['a','i','u','e','o']]))





# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
