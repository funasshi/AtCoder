# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)



x,y = list(map(int, input().split()))

if x-y>3 or y-x>2:
    print("No")
else:
    print("Yes")


# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
