n = int(input())


candidate = [1]

kouho = 6
while n >= kouho:
    candidate.append(kouho)
    kouho *= 6
kouho = 9
while n >= kouho:
    candidate.append(kouho)
    kouho *= 9

candidate.sort()

ans = 0
while n:
    big = candidate.pop()
    if big <= n:
        n -= big
        ans += 1
        candidate.append(big)

print(ans)
