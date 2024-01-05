# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = input()

pre_number=0

flag=0
for i in range(len(n)):
    if i==0:
        pre_number=n[i]
    else:
        number=n[i]
        if number>=pre_number:
            flag=1
            break
        pre_number=number

if flag==0:
    print('Yes')
else:
    print("No")



# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
