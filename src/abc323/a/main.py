# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


s = input()

if s[1::2]=='00000000':
    print("Yes")
else:
    print("No")

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
