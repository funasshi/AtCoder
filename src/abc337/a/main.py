# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
x_sum,y_sum=0,0

for i in range(n):
    x, y = list(map(int, input().split()))
    x_sum+=x
    y_sum+=y

if x_sum>y_sum:
    print("Takahashi")
elif x_sum<y_sum:
    print("Aoki")
else:
    print("Draw")
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
