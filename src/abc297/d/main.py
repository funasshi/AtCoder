a, b = map(int, input().split())

ans=0
while a!=b:
    if a>b:
        if a%b==0:
            ans+=a//b-1
            a=b
        else:
            ans+=a//b
            a=a%b
    if b>a:
        if b%a==0:
            ans+=b//a-1
            b=a
        else:
            ans+=b//a
            b=b%a
print(ans)
