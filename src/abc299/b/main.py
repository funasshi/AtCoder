# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n,t= list(map(int, input().split()))
c_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

if not t in c_list:
    t=c_list[0]
index=0
maxNum=0
for i in range(n):
    if c_list[i]==t:
        if maxNum<r_list[i]:
            maxNum=max(maxNum,r_list[i])
            index=i
    
# n, m = list(map(int, input().split()))

print(index+1)
# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
