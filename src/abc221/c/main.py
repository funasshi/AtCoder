n=input()

def split_two(pattern):
    num=list(n)
    one=[]
    two=[]
    for i in range(len(n)):
        if pattern[i]=="0":
            one.append(n[i])
        else:
            two.append(n[i])
    one.sort(reverse=True)
    two.sort(reverse=True)
    one="".join(list(map(str,one)))
    two="".join(list(map(str,two)))
    return int(one),int(two)

max_ans=0
for i in range(1,2**len(n)-1):
    pattern=format(i,"0"+str(len(n))+"b")
    one,two=split_two(pattern)
    max_ans=max(max_ans,one*two)
    if max_ans==630:
        pass
print(max_ans)