h,w,k=[int(i) for i in input().split()]

def get_conbination(i,length):
    return format(i, '#0'+str(length+2)+'b')[2:]
sheet=[]
for i in range(h):
    sheet.append(input())

ans=0
for i in range(2**h):
    for j in range(2**w):
        total=0
        gyou_select=get_conbination(i,h)
        retu_select = get_conbination(j, w)
        for gyou in range(h):
            for retu in range(w):
                if gyou_select[gyou]=="0" and retu_select[retu]=="0":
                    if sheet[gyou][retu]=="#":
                        total+=1
        if total==k:
            ans+=1

print(ans)

