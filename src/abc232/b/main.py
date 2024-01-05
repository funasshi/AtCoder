
def char2num(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(char)


s = list(map(char2num, list(input())))
t = list(map(char2num, list(input())))

one = s[0]
two = t[0]

add = (two-one) % 26

for i in range(len(s)):
    s[i] = (s[i]+add) % 26

flag = 0
for i in range(len(s)):
    if s[i] != t[i]:
        flag = 1

if flag == 0:
    print("Yes")
else:
    print("No")
