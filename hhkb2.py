h,w=[int(i) for i in input().split()]
masu=[list(input()) for i in range(h)]


def num_able_to_huton(i,j):
    ans=0
    if masu[i][j]=="#":
        return ans
    kouho=[]
    if i!=h-1:
        kouho.append([i+1,j])
    if i!=0:
        kouho.append([i -1,j])
    if j!=w-1:
        kouho.append([i,j+1])
    if j!=0:
        kouho.append([i,j-1])
    for x,y in kouho:
        if masu[x][y]==".":
            ans+=1
    return ans

ans=0
for i in range(h):
    for j in range(w):
        ans+=num_able_to_huton(i, j)

print(ans//2)
