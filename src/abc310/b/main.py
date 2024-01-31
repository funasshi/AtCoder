# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n,m= list(map(int, input().split()))


class Item:
    def __init__(self,price,functions) -> None:
        self.price=price
        self.functions=functions

item_list=[]
for i in range(n):
    p,c,*f= list(map(int, input().split()))
    item_list.append(Item(p,f))

def check(i,j):
    one=item_list[i]
    two=item_list[j]
    if one.price<two.price:
        return False
    if set(two.functions)>=set(one.functions):
        if one.price>two.price or len(two.functions)>len(one.functions):
            return True
    return False
        

flag=0 
for i in range(n):
    for j in range(n):
        if check(i,j):
            flag=1

if flag:
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
