h, w = map(int, input().split())
sheet = []

for i in range(h):
    sheet.append(list(map(int, input().split())))

ans = []
for i, row in enumerate(sheet):
    for j, num in enumerate(row):
        if j != w-1:
            if num % 2 == 1:
                ans.append([i+1, j+1, i+1, j+2])
                sheet[i][j] -= 1
                sheet[i][j+1] += 1


new_sheet = []
for row in sheet:
    new_sheet.append(row[-1])
j = w-1
for i, num in enumerate(new_sheet):
    if num % 2 == 1 and i != h-1:
        ans.append([i+1, j+1, i+2, j+1])
        new_sheet[i] -= 1
        new_sheet[i+1] += 1

n = len(ans)
print(n)
for shuturyoku in ans:
    print(*shuturyoku)
