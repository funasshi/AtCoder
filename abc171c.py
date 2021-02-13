n=int(input())

alphabet="abcdefghijklmnopqrstuvwxyz"
def get_keta(n):
    i=1
    check=26
    while True:
        if n<=check:
            return i
        check=check*26+26
        i+=1

def get_new_n(n, keta):
    new_n = n
    for i in range(1, keta):
        new_n -= 26 ** i
    return new_n

keta=get_keta(n)
n=get_new_n(n,keta)-1
ans=[]
for i in range(keta):
    ans.append(alphabet[n%26])
    n-=n%26
    n=n//26

print("".join(ans)[::-1])





