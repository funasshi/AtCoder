# 二分探索
# functionを満たす,search_listの最大の要素を出力
# 【注意点】searchリストの初めの方はfunctionを満たし、後ろに行くにつれて満たさなくなるべき
import math
import sys
sys.setrecursionlimit(10**9)
def binary_research(start,end,function):
    if start==end:
        return start
    middle=math.ceil((start+end)/2)
    if function(middle):
        start=middle
    else:
        end=middle-1
    return binary_research(start, end, function)
a,b,x=[int(i) for i in input().split()]

def function(n):
    if x>=a*n+b*len(str(n)):
        return True
    return False

print(binary_research(0,10**9,function))

