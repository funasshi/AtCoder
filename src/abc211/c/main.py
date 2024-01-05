s="."+input()
n=len(s)-1
mod=10**9+7
c=[0]*(n+1)
ch=[0]*(n+1)
cho=[0]*(n+1)
chok=[0]*(n+1)
choku=[0]*(n+1)
chokud=[0]*(n+1)
chokuda=[0]*(n+1)
chokudai=[0]*(n+1)

# c
for i in range(1,n+1):
    if s[i]=="c":
        c[i]=(c[i-1]+1)%mod
    else:
        c[i]=c[i-1]

# ch

for i in range(1,n+1):
    if s[i]=="h":
        ch[i]=(c[i-1]+ch[i-1])%mod
    else:
        ch[i]=ch[i-1]

# cho
for i in range(1,n+1):
    if s[i]=="o":
        cho[i]=(ch[i-1]+cho[i-1])%mod
    else:
        cho[i]=cho[i-1]

# chok
for i in range(1,n+1):
    if s[i]=="k":
        chok[i]=(cho[i-1]+chok[i-1])%mod
    else:
        chok[i]=chok[i-1]

# choku
for i in range(1,n+1):
    if s[i]=="u":
        choku[i]=(chok[i-1]+choku[i-1])%mod
    else:
        choku[i]=choku[i-1]

# chokud
for i in range(1,n+1):
    if s[i]=="d":
        chokud[i]=(choku[i-1]+chokud[i-1])%mod
    else:
        chokud[i]=chokud[i-1]

# chokuda
for i in range(1,n+1):
    if s[i]=="a":
        chokuda[i]=(chokud[i-1]+chokuda[i-1])%mod
    else:
        chokuda[i]=chokuda[i-1]

# chokudai
for i in range(1,n+1):
    if s[i]=="i":
        chokudai[i]=(chokuda[i-1]+chokudai[i-1])%mod
    else:
        chokudai[i]=chokudai[i-1]

print(chokudai[-1])