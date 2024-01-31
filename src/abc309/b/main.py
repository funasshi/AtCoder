# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
graph=[]
new_graph=[]
for i in range(n):
    input_list=list(input())
    graph.append(input_list.copy())
    new_graph.append(input_list.copy())

def rotate():
    for i in range(n):
        if i==0:
            continue
        else:
            new_graph[0][i]=graph[0][i-1]
            new_graph[-1][-i-1]=graph[-1][-i]
            new_graph[-1-i][0]=graph[-i][0]
            new_graph[i][-1]=graph[i-1][-1]
rotate()
for new_list in new_graph:
    print("".join(new_list))

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
