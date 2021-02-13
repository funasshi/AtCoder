n=int(input())

zorome_max=0
zorome=0

for i in range(n):
    one,two=[int(i) for i in input().split()]
    if one==two:
        zorome+=1
        zorome_max=max(zorome_max,zorome)
    else:
        zorome=0

if zorome_max>=3:
    print("Yes")
else:
    print("No")

