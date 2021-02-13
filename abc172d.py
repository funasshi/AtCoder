n=int(input())

def number_of_divisor(n):
    ans=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            ans[j]+=1
    return ans

divisor=number_of_divisor(n)
ans=0
for i in range(1,n+1):
    ans+=i*divisor[i]

print(ans)

