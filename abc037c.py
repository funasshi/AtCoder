n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

number_of_bubunretu=n-k+1

# 1~k番目はmin(1~k,n-k+1)回
# 終わりから1~k番目はmin(1~k,n-k+1)回
# 始まりからk+1番目~終わりからk+1番目はmin(k,n-k+1)回

plus_times=[0]*n

for i in range(k):
    plus_times[i]=min(i+1,n-k+1)
    plus_times[-i-1] = min(i + 1, n - k + 1)
if k+1<n-k+1:
    for i in range(k,n-k+1):
        plus_times[i]=k
ans=0
for i in range(n):
    ans+=a[i]*plus_times[i]

print(ans)


