n = int(input())
gyouretu = []
for i in range(n):
    gyouretu.append(list(map(int, list(input()))))


def move(direction, now):
    return [(now[0]+direction[0]) % n, (now[1]+direction[1]) % n]


directions = [[1, 0], [0, 1], [-1, 0], [0, -1],
              [1, 1], [1, -1], [-1, 1], [-1, -1]]

ans_list = []
for direction in directions:
    for start_i in range(n):
        for start_j in range(n):
            ans = str(gyouretu[start_i][start_j])
            i = start_i
            j = start_j
            for _ in range(n-1):
                [i, j] = move(direction, [i, j])
                ans += str(gyouretu[i][j])
            ans_list.append(int(ans))

print(max(ans_list))
