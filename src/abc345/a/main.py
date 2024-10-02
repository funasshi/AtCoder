# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


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
s=input()

def check(s):
    if s[0]!='<':
        return False
    if s[-1]!='>':
        return False
    between=s[1:-1]
    if len(set(between))==1 and between[0]=='=':
        return True
    return False

if check(s):
    print("Yes")
else:
    print("No")