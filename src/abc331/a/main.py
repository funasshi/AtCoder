# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


# n = int(input())
M,D = list(map(int, input().split()))
y,m,d = list(map(int, input().split()))

if m==M and d==D:
    new_y=y+1
else:
    new_y=y

if d==D:
    if m==M:
        new_m=1
    else:
        new_m=m+1
    new_d=1
else:
    new_m=m
    new_d=d+1
    
print(new_y,new_m,new_d)

# a_list = list(map(int, input().split()))

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
