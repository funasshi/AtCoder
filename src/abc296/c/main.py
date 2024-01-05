import sys
sys.setrecursionlimit(10 ** 9)


n,x = list(map(int, input().split()))
a_list = list(map(int, input().split()))

a_list.sort()

sentou=0
matubi=0


def sa(i,j):
    return a_list[j]-a_list[i]

def f(sentou,matubi):
    if matubi>=n or sentou>=n:
        return False
    diff=sa(sentou,matubi)
    if diff<x:
        matubi+=1
        return f(sentou,matubi)
    elif diff>x:
        sentou+=1
        return f(sentou,matubi)
    elif diff==x:
        return True
    else:
        return False

if f(sentou,matubi):
    print("Yes")
else:
    print("No")
