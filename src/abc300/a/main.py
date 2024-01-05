# from scipy.sparse import csr_matrix8G
import sys
sys.setrecursionlimit(10**9)


n, a, b = list(map(int, input().split()))
c_list=list(map(int,input().split()))

ans=a+b


print(c_list.index(ans)+1)
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
