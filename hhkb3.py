import sys

sys.setrecursionlimit(10**8)


n=int(input())
p=[int(i) for i in input().split()]

counter=[0]*300000
now=0

def assess():
    global now
    if counter[now]!=0:
        now+=1
        assess()
    else:
        print(now)

for i in p:
    counter[i]=1
    assess()

