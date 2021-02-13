n=int(input())
a=[int(i) for i in input().split()]

def renzoku_list(a):
    ans_list=[]
    pre_num=None
    renzoku=0
    for i in a:
        if pre_num==None:
            pre_num=i
            renzoku=1
        elif pre_num<i:
            renzoku+=1
            pre_num=i
        else:
            if renzoku!=1:
                ans_list.append(renzoku)
            pre_num=i
            renzoku=1
    if renzoku!=1:
        ans_list.append(renzoku)
    return ans_list

ans_list=renzoku_list(a)

ans=n
for i in ans_list:
    ans+=i*(i-1)//2
print(ans)
