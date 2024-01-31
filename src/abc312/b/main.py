# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n,m= list(map(int, input().split()))
s_list=[]
for i in range(n):
    s_list.append(input())

def isTakCode(masu):
    for i in [0,1,2,3]:
        for j in [0,1,2,3]:
            if i==3 or j==3:
                if masu[i][j]!='.':
                    return False
            else:
                if masu[i][j]!='#':
                    return False
    for i in [5,6,7,8]:
        for j in [5,6,7,8]:
            if i==5 or j==5:
                if masu[i][j]!='.':
                    return False
            else:
                if masu[i][j]!='#':
                    return False
    return True

ans=[]
def genTakCode(h,w):
    takCode=[]
    for i in range(h,h+9):
        takCode.append(s_list[i][w:w+9])
    return takCode
    

for h in range(n-8):
    for w in range(m-8):
        takCodable=genTakCode(h,w)
        if isTakCode(takCodable):
            ans.append([h+1,w+1])
# n, m = list(map(int, input().split()))
for i ,j in ans:
    print(i,j)

if len(ans)==0:
    print()

# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
