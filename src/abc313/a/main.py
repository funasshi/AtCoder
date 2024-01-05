# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
p_list = list(map(int, input().split()))


a=p_list[0]
if n==1:
    print(0)
else:
    
    max_p=max(p_list[1:])

    print(max(max_p-a+1,0))
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
