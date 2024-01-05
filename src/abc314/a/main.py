# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)

pi='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'


n = int(input())


print(pi[:n+2])

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
