x,k,d=[int(i) for i in input().split()]

x=abs(x)
if x-k*d>=0:
    print(x-k*d)
else:
    if (x//d)%2==k%2:
        print(x%d)
    else:
        print(d-x%d)