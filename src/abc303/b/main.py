# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n, m = list(map(int, input().split()))
jyunban_map=[]
for i in range(m):
    jyunban_map.append(list(map(lambda x:int(x)-1, input().split())))
nakayoshi_list=[[0 for i in range(n)] for j in range(n)]

for jyunban in jyunban_map:
    for i in range(n-1):
        one=jyunban[i]
        two=jyunban[i+1]
        if one>two:
            one,two=two,one
        nakayoshi_list[one][two]=1
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if nakayoshi_list[i][j]==0:
            count+=1

print(count)

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
