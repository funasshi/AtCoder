n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

a_count=[0]*(n+1)
b_count=[0]*(n+1)


def new_order(a,b):
    import queue
    import random
    ideal_number_getter=queue.Queue()
    ans_list=[]
    random.shuffle(b)
    for i in b:
        ideal_number_getter.put(i)
    # for i in range((n//3)*2):
    #     tmp=ideal_number_getter.get()
    #     ideal_number_getter.put(tmp)

    for i in range(n):
        while True:
            new=ideal_number_getter.get()
            if a[i]==new:
                ideal_number_getter.put(new)
            else:
                ans_list.append(str(new))
                break
    return " ".join(ans_list)



for i in a:
    a_count[i]+=1
for i in b:
    b_count[i]+=1

ans=0
for i in range(1,n+1):
    if not a_count[i]+b_count[i]<=n:
        ans+=1
if ans==0:
    print("Yes")
    print(new_order(a,b))

else:
    print("No")