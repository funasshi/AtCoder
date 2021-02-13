s=input()
t=input()
lt=len(t)
ls=len(s)

def get_times(head,s,t):
    count = 0
    for i,j in enumerate(range(head,lt+head)):
        if s[j]!=t[i]:
            count+=1
    return count

ans=100000000000000
for i in range(ls-lt+1):
    ans=min(ans,get_times(i,s,t))
print(ans)