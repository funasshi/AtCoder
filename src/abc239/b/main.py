x = input()
sign = "+"
if x[0] == "-":
    sign = "-"
else:
    sign = "+"

if len(x) == 1:
    print(0)
elif sign == "+":
    print(int(x[:-1]))
else:
    if len(x) == 2:
        print(-1)
    elif x[-1] == "0":
        print(int(x[:-1]))
    else:
        print(int(x[:-1])-1)
