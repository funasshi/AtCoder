n,m = list(map(int, input().split()))
a= list(map(int, input().split()))
b= list(map(int, input().split()))

a.sort()
b.sort()

INF=10**12
now_a=0
now_b=0


min_sa=INF
while now_a<n and now_b<m:
    sa=abs(a[now_a]-b[now_b])
    min_sa=min(min_sa,sa)
    if a[now_a]>b[now_b]:
        now_b+=1
    else:
        now_a+=1

print(min_sa)