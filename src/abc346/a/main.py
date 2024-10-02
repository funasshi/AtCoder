# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
a_list = list(map(int, input().split()))

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
ans=[]
for i in range(n-1):
    ans.append(a_list[i]*a_list[i+1])

print(*ans)