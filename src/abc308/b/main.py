# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n,m= list(map(int, input().split()))
c_list = input().split()
d_list = input().split()
p_list = list(map(int, input().split()))
ans=0
for color in c_list:
    if color in d_list:
        ans+=p_list[d_list.index(color)+1]
    else:
        ans+=p_list[0]

print(ans)


# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
