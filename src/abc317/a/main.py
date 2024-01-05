# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)



n,h,x = list(map(int, input().split()))
p_list = list(map(int, input().split()))

a=x-h
print(len([i for i in p_list if i<a])+1)
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
