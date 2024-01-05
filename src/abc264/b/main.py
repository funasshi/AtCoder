r,c = list(map(int, input().split()))
hyou=[[None for i in range(15)] for i in range(15)]

def tate_start(i):
    return i

def yoko_start(i):
    return i

def last_length(i):
    return 15-2*i

white="."
black="#"

for i in range(8):
    for x in range(tate_start(i),tate_start(i)+last_length(i)):
        for y in range(yoko_start(i),yoko_start(i)+last_length(i)):
            if i%2==0:
                hyou[x][y]=black
            else:
                hyou[x][y]=white


ans=hyou[r-1][c-1]
if ans==white:
    print("white")
else:
    print("black")
