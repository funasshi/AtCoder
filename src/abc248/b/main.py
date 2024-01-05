import math
a, b, k = list(map(int, input().split()))

i = 0
flag = 0
while flag == 0:
    if math.log(k)*i >= math.log(b/a):
        print(i)
        flag = 1
    else:
        i += 1
