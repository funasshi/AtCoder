n=int(input())
a=[int(i) for i in input().split()]

total=sum(a)

count=[0]*(10**5+1)

for i in a:
    count[i]+=1

q=int(input())
for i in range(q):
    b,c=[int(i) for i in input().split()]
    total+=(c-b)*count[b]
    count[c]+=count[b]
    count[b] = 0
    print(total)