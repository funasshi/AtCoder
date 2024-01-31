# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


h,w=list(map(int, input().split()))

a=[]

for i in range(h):
   a.append(list(input()))

b=[]

for i in range(h):
   b.append(list(input()))
def up_shift(matrix,n):
   new_matrix=[["." for i in range(w)] for i in range(h)]
   for x in range(w):
      for y in range(h):
         new_matrix[y][x]=matrix[(y+n)%h][x]
   return new_matrix

def right_shift(matrix,n):
   new_matrix=[["." for i in range(w)] for i in range(h)]
   for x in range(w):
      for y in range(h):
         new_matrix[y][x]=matrix[y][(x+n)%w]
   return new_matrix

def equal(a,b):
   for x in range(w):
      for y in range(h):
         if not a[y][x]==b[y][x]:
            return False
   return True


flag=0

for x in range(w):
   for y in range(h):
      new_a=up_shift(a,y)
      new_a=right_shift(new_a,x)
      if equal(new_a,b):
         flag=1

if flag==1:
   print("Yes")
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
