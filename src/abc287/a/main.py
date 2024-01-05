n = int(input())
ans = 0
for i in range(n):
    if input() == "For":
        ans += 1
if ans*2 >= n:
    print("Yes")
else:
    print("No")
