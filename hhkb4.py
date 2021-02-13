t=int(input())

mod=10**9+7

def wa(n):
    return (n*(n+1))//2

def jkljkjk():
    n,a,b=[int(i) for i in input().split()]
    if n-a-b+1>0:
        return 4*((n-b+1)*(n-a+1)*wa(n-a-b+1)-wa(n-a-b+1)**2)
    else:
        return 0

for i in range(t):
    print(jkljkjk()%mod)
