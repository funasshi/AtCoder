s = input()

if s in ["o", "x", "ox", "xo", "xx", "oxo", "xoo", "oox"]:
    print("Yes")
elif len(s) <= 3:
    print("No")
else:
    if s[0] == "o":
        start = 0
    elif s[1] == "o":
        start = 1
    else:
        start = 2
    if s[-1] == "o":
        end = -1
    elif s[-2] == "o":
        end = -2
    else:
        end = len(s)
    middle = s[start:end]
    if len(middle) % 3 == 0:
        x = len(middle)//3
        if middle == "oxx"*x:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
