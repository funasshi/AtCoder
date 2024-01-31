# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))

b=[]
for i in range(n):
    b.append(list(map(int,input().split())))

def rotate(a):
    new_a=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i]=a[i][j]
    return new_a

def check(a,b):
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and b[i][j]==0:
                return False
    return True
flag=0
for i in range(4):
    a=rotate(a)
    if check(a,b):
        flag=1

if flag==0:
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
