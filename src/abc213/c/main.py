h,w,n = list(map(int, input().split()))
a_list=[]
b_list=[]
import copy
for i in range(n):
    a,b=list(map(int,input().split()))
    a_list.append(a)
    b_list.append(b)


a_check=list(set(copy.copy(a_list)))
a_check.sort()

a_dict={}
for i,a in enumerate(a_check):
    if a not in a_dict:
        a_dict[a]=i


b_check=list(set(copy.copy(b_list)))
b_check.sort()
b_dict={}
for i,b in enumerate(b_check):
    if b not in b_dict:
        b_dict[b]=i

a_ans=[a_dict[i]+1 for i in a_list]
b_ans=[b_dict[i]+1 for i in b_list]


for i in range(n):
    print(a_ans[i],b_ans[i])