n,y=[int(i) for i in input().split()]

def get():
    for num_10000 in range(n+1):
        for num_5000 in range(n-num_10000+1):
            num_1000=n-num_10000-num_5000
            if y==10000*num_10000+5000*num_5000+1000*num_1000:
                return [num_10000,num_5000,num_1000]
    return [-1,-1,-1]
a,b,c=get()

print(a,b,c)

