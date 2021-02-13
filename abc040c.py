n=int(input())
a=[int(i) for i in input().split()]

dp=[None]*(n)
for i in range(n):
    if i==0:
        dp[0]=0
    elif i==1:
        dp[1]=abs(a[1]-a[0])
    else:
        dp[i]=min(dp[i-2]+abs(a[i-2]-a[i]),dp[i-1]+abs(a[i]-a[i-1]))

print(dp[-1])

