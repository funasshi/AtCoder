import math
n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]


def get_1_index(a):
    for i,j in enumerate(a):
        if j==1:
            return i


index=get_1_index(a)

mae=index
usiro=n-index-1

# print(math.ceil(mae/(k-1))+math.ceil(usiro/(k-1)))
print(math.ceil((n-1)/(k-1)))