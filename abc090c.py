n,m=[int(i) for i in input().split()]



if n!=1 and m!=1:
    print(max(0,(n-2)*(m-2)))
elif n==1 and m==1:
    print(1)
elif n==1 or m==1:
    print(max(n,m)-2)
