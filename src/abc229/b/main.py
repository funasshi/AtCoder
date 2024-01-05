a, b = input().split()
length = min(len(a), len(b))
kuriagari = 0
for i in range(length):
    one = int(a[-i-1])
    two = int(b[-i-1])
    if one+two >= 10:
        kuriagari = 1

if kuriagari == 0:
    print("Easy")
else:
    print("Hard")
