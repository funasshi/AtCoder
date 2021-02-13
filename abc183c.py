import itertools
n, k = [int(i) for i in input().split()]
time_cost = []

for _ in range(n):
    time_cost.append([int(i) for i in input().split()])

ans = 0
for order in list(itertools.permutations(range(1, n))):
    start = 0
    time = 0
    for town in order:
        end = town
        time += time_cost[end][start]
        start = town
    time += time_cost[0][start]
    if time == k:
        ans += 1

print(ans)
