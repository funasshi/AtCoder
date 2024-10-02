# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


# n = int(input())
# a, b, c = list(map(int, input().split()))
# a_list = list(map(int, input().split()))

# # n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
s=input()

a,b=list(set(list(s)))

a_count=s.count(a)
b_count=s.count(b)

if a_count<b_count:
    a,b=b,a

print(s.index(b)+1)