# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())

s_list=[]
a_list=[]
for i in range(n):
    s,a=input().split()
    a=int(a)
    s_list.append(s)
    a_list.append(a)
min_index=a_list.index(min(a_list))
new_list=s_list[min_index:]+s_list[:min_index]
for i in new_list:
    print(i)


#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
