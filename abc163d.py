n,k=[int(i) for i in input().split()]
mod=10**9+7
def part_sum(start,k):
    return k*(k+1)//2+(k*(start-1))

def count_sum(k):
    return part_sum(n-k+1,k)-part_sum(0,k)+1
ans=0
for i in range(k,n+2):
    ans+=count_sum(i)
    ans=ans%mod
print(ans)