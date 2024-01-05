n = int(input())
s_list = list(map(int, input().split()))

kouho_list = []

for a in range(1, 1000):
    for b in range(1, 1000):
        kouho_list.append(4*a*b+3*a+3*b)


ans = 0

for s in s_list:
    if s not in kouho_list:
        ans += 1
print(ans)
