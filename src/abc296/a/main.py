n = int(input())
s=input()

if len(s)==1:
    print("Yes")
else:
    s1=s[::2]
    s2=s[1::2]

    if s[0]!=s[1] and len(set(s1))==1 and len(set(s2))==1:
        print("Yes")
    else:
        print("No")