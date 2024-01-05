n,k = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list=[]
for j,a in enumerate(a_list):
    for i in range(1,2*10**2):
        b_list.append([a*i,j])
b_list=list(set(b_list))
b_list.sort(key=lambda x:x[0])

sabun=[]
for i in range(len(b_list)):
    if i==0:
        sabun.append(b_list[i][0])
    else:
        sabun.append(b_list[i][0]-b_list[i-1][0])

def get_sorted_index_list(lst):
    return [i[0] for i in sorted(enumerate(lst), key=lambda x: x[1])]

sabun_sort_index=get_sorted_index_list(sabun)

now=[0]*len(n)


def sabunOk(index):
    if sabun[index]==0:
        return False
    if index==0:
        return True
    else:
        b_list[index-1][1]

ans=0

for i in range(k):
    for sabun_index in sabun_sort_index:
        if sabunOk(sabun_index):
            now[sabun_index]+=1
            if sabun_index!=0:
                now[sabun_index-1]-=1
            ans+=sabun[sabun_index]
            break
print(ans)
