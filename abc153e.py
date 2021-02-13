h, n = [int(i) for i in input().split()]

magics = [None]


class Magic:
    def __init__(self, attack, cost):
        self.attack = attack
        self.cost = cost


maxA = 0
for i in range(n):
    attack, cost = [int(i) for i in input().split()]
    maxA = max(maxA, attack)
    magics.append(Magic(attack, cost))

dp = [[10 ** 9 for i in range(h + maxA)] for j in range(n + 1)]

for i in range(n + 1):
    for j in range(h + maxA):
        if j == 0:
            dp[i][j] = 0
        elif i == 0:
            continue
        elif j - magics[i].attack >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - magics[i].attack] + magics[i].cost)
        else:
            dp[i][j] = dp[i - 1][j]

print(min(dp[-1][h:]))
