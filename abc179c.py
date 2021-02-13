n=int(input())

def kouho_num(a):
    if n%a==0:
        return n//a-1
    else:
        return n//a
ans=0

for i in range(1,n):
    ans+=kouho_num(i)
print(ans)