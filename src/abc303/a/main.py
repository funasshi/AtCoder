# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
s=input()
t=input()

flag=0
for i in range(n):
    if s[i] in ['0','o'] and t[i] in ['0','o']:
        continue
    if s[i] in ['1','l'] and t[i] in ['1','l']:
        continue
    if s[i]==t[i]:
        continue
    flag=1

if flag==1:
    print("No")
else:
    print("Yes")
# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
