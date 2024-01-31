# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


p,q=input().split()

haba=[3,1,4,1,5,9]
alphabet="ABCDEFG"

p=alphabet.index(p)
q=alphabet.index(q)

if p>q:
    p,q=q,p
    

print(sum(haba[p:q]))


# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
