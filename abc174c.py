k = int(input())
seven = 0
i = 0
if k % 2 == 0:
    print(-1)
else:
    while True:
        i += 1
        seven = seven * 10 + 7
        seven = seven % k
        if seven == 0:
            print(i)
            break
        if i>1000000:
            print(-1)
            break
