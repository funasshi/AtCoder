x,n=[int(i) for i in input().split()]
p=[int(i) for i in input().split()]
p.sort()
p_non=[]


for i in range(102):
    if i not in p:
        p_non.append(i)
p_non.sort()

zettaiti=1000000
ans=None
for i in p_non:
    if abs(i-x)<zettaiti:
        ans=i
        zettaiti=abs(i-x)

print(ans)