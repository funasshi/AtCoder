N = int(input())
S = [0]+list(map(int, input().split()))

a=[0]*(N+1)
for i in range(1,N+1):
    a[i]=S[i]-S[i-1]

print(*a[1:])
