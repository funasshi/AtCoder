n,x,m=[int(i) for i in input().split()]
x_amari=x%m
amari=[]

for i in range(m):
    amari.append(x_amari)
    x_amari=(x_amari**2)%m

def chouhuku_index(amari):
    index = [0] * m
    for j,i in enumerate(amari):
        if index[i]==0:
            index[i]+=1
        else:
            end=j
            tyouhuku=i
            break
    for j,i in enumerate(amari):
        if i==tyouhuku:
            start=j
            break
    return start,end

start,j=chouhuku_index(amari)

new_amari=amari[:j+1]

#ループが途切れ、ずっと同じ時
if new_amari[-1]==new_amari[-2]:
    front=sum(new_amari[:-2])+(x//m)*m
    back=new_amari[-1]*(n-j)
    print(front+back)
else:#ループし続ける
    end=j
    new_amari = new_amari[:-1]
    front=sum(new_amari[:start])+(x//m)*m
    n=n-start
    roop_shuki=end-start
    tyuukann=sum(new_amari[start:])*(n//roop_shuki)
    back=sum(new_amari[start:start+n%roop_shuki])
    print(front+tyuukann+back)