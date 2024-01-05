n, m= list(map(int, input().split()))
a_list= list(map(int, input().split()))

is_read=[False]*(n+1)

ans=[]

def read(n):
    if n in a_list:
        read(n+1)
    is_read[n]=True
    ans.append(n)

for i in range(1,n+1):
    if not is_read[i]:
        read(i)
print(*ans)