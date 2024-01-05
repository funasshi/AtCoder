n = int(input())
h = list(map(int, input().split()))

now = 0

for next_height in h:
    if now < next_height:
        now = next_height
    else:
        break
print(now)
