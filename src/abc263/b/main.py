N = int(input())
parents = [-1,-1]+list(map(int,input().split()))


a=-1
ans=1
while True:
    if parents[a]==1:
        break
    else:
        a=parents[a]
        ans+=1

print(ans)