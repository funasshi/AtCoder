n,m,x=[int(i) for i in input().split()]

books=[]

for i in range(n):
    books.append([int(i) for i in input().split()])


# ==================================================-
# 整数を２進数に変換
def get_conbination(i,length):
    return format(i, '#0'+str(length+2)+'b')[2:]

min_cost=100000000000000
for i in range(2**n):
    rikai=[0]*m
    select=get_conbination(i,n)
    cost=0
    for j in range(n):
        if select[j] == "1":
            for k in range(m):
                rikai[k]+=books[j][k+1]
            cost+=books[j][0]
    if min(rikai)>=x:
        min_cost=min(min_cost,cost)

if min_cost==100000000000000:
    print(-1)
else:
    print(min_cost)
