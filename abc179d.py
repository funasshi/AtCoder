mod=998244353

n,k=[int(i) for i in input().split()]
s=[]
for i in range(k):
    l, r = [int(i) for i in input().split()]
    for j in range(l,r+1):
        s.append(j)
s.sort()

#sをつかってn-1をつくるのが何通りかを調べればいい

def huteihouteisiki(keisuu,uhen):
    mod=998244353
    if len(keisuu)==1:
        if uhen%keisuu[0]==0:
            return 1
    max_keisuu=keisuu[-1]
    ans=0
    for i in range(uhen//max_keisuu+1):
        new_uhen=uhen-max_keisuu*i
        new_keisuu=keisuu[:-1]
        ans+=huteihouteisiki(new_keisuu,new_uhen)
    return ans%mod

print(huteihouteisiki(s,n-1))
