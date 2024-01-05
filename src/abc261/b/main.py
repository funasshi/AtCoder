n = int(input())
hyou=[]
for i in range(n):
    hyou.append(input())


def hantei(a,b):
    if a=="W" and b=="L":
        return True
    if a=="L" and b=="W":
        return True
    if a=="D" and b=="D":
        return True
    return False

mujyun=0
for i in range(n):
    for j in range(i+1,n):
        if not hantei(hyou[i][j],hyou[j][i]):
            mujyun=1

if mujyun==1:
    print("incorrect")
else:
    print("correct")