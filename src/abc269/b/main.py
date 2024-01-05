def find_ABCD(s):
    a,b,c,d=None,None,None,None
    for i in range(10):
        if "#" in s[i] and a is None:
            a=i+1
            c=s[i].index("#")+1
            d=10-s[i][::-1].index("#")
        if a is not None and "#" not in s[i]:
            b=i
            break
    if b==None:
        b=10
    return a,b,c,d
s=[]
for i in range(10):
    s.append(input())
a,b,c,d=find_ABCD(s)

print(a,b)
print(c,d)
