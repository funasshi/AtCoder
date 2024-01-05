# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
s=input()

flag=0
for i in range(n-2):
    if s[i:i+3]=='ABC':
        print(i+1)
        flag=1
        break
    
if flag==0:
    print(-1)

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
