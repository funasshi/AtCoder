# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
a_list = list(map(int, input().split()))

ans_list=[]

for i in range(n):
    if i==0:
        ans_list.append(a_list[i])    
    else:
        pre=ans_list[-1]
        now=a_list[i]
        if pre>now:
            for num in range(pre-1,now-1,-1):
                ans_list.append(num)
        else:
            for num in range(pre+1,now+1):
                ans_list.append(num)

print(*ans_list)

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
