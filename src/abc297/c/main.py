h,w = list(map(int, input().split()))

s_list=[]

for i in range(h):
    s_list.append(input())


def henkan(s):
    ans=''
    sentou=0
    while sentou<w-1:
        if s[sentou]=='T' and s[sentou+1]=='T':
            ans=ans+"PC"
            sentou+=2
        else:
            ans=ans+s[sentou]
            sentou+=1
    if len(ans)!=w:
        ans+=s[-1]
    return ans

for s in s_list:
    print(henkan(s))