s=input()
n=len(s)//2


taishou=list(s)

for i in range(n):
    taishou[2*i],taishou[2*i+1]=taishou[2*i+1],taishou[2*i]

print("".join(taishou))