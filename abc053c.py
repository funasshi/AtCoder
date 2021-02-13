x=int(input())

ans=(x//11)*2
if x%11==0:
    pass
elif 0<x%11<=6:
    ans+=1
else:
    ans+=2
print(ans)
