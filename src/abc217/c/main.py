n = int(input())
p_list = list(map(int, input().split()))

q=[0]*n

for i,p in enumerate(p_list):
    q[p-1]=i+1

print(*q)