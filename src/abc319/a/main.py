# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)

a={
    'tourist':3858,
'ksun48': 3679,
'Benq' :3658,
'Um_nik': 3648,
'apiad':3638,
'Stonefeang': 3630,
'ecnerwala': 3613,
'mnbvmar': 3555,
'newbiedmy': 3516,
'semiexp': 3481,

}
s=input()
print(a[s])
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
