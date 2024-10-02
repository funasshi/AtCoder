# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


# n = int(input())
a, b, d = list(map(int, input().split()))
# a_list = list(map(int, input().split()))

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)
ans=[]
# matrix = csr_matrix((data, (row, col)), (n, n))
end=a
while end!=b:
    ans.append(end)
    end+=d
ans.append(b)
print(*ans)