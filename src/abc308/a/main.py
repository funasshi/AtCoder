# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


s_list = list(map(int, input().split()))
max_s=max(s_list)
min_s=min(s_list)
flag=0

if not 100<=min_s<=max_s<=675:
    flag=1

for i in s_list:
    if not i%25==0:
        flag=1

sorted_s_list=sorted(s_list)

for i in range(len(s_list)):
    if not s_list[i]==sorted_s_list[i]:
        flag=1
        
if flag==1:
    print("No")
else:
    print("Yes")
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
