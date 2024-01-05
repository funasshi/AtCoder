s = input()
if "a" in list(s):
    for i in range(len(s)):
        if s[len(s)-i-1] == "a":
            print(len(s)-i)
            break
else:
    print(-1)
