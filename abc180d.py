import math
x, y, a, b = [int(i) for i in input().split()]

k = max(int(math.log(b/((a-1)*x), a))+1, 1)

if x >= b/(a-1):
    k = 0
remain = y-x*(a**k)
if remain > 0:
    if remain % b == 0:
        k += remain//b-1
    else:
        k += remain//b
else:
    k = 0

print(k)
