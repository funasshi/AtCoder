hyou=[]

x=None
y=None

for i in range(8):
    s=input()
    if "*" in s:
        x=8-i
        y=s.index('*')


alpha='abcdefgh'

print(alpha[y]+str(x))