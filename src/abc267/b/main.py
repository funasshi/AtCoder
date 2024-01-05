s=[int(i) for i in list("0"+input())]

pattern=[]

pattern.append(s[7])
pattern.append(s[4])
pattern.append(s[2]+s[8])
pattern.append(s[1]+s[5])
pattern.append(s[3]+s[9])
pattern.append(s[6])
pattern.append(s[10])


def jyouken1(i,j):
    return pattern[i]>=1 and pattern[j]>=1

def jyouken2(i,j):
    if abs(j-i)==1:
        return False
    for k in range(i+1,j):
        if pattern[k]==0:
            return True
    return False

def split():
    if not s[1]==0:
        return False
    
    for i in range(6):
        for j in range(i+1,7):
            if jyouken1(i,j) and jyouken2(i,j):
                return True
    return False

if split():
    print("Yes")
else:
    print("No")