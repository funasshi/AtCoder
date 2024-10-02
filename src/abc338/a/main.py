# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)

s=input()

if len(s)==1:
    if s.upper()==s:
        print("Yes")
    else:
        print("No")
else:
    s_front=s[0]
    s_end=s[1:]
    if s_front.upper()==s_front and s_end.lower()==s_end:
        print("Yes")
    else:
        print("No")

# n = int(input())
# a, b, c = list(map(int, input().split()))
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
