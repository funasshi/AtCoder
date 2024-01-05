r,c=map(int,input().split())
sheet=[]
for i in range(r):
    sheet.append(list(input()))


def manhattan_coordinates(i, j,n):
    result = [(i,j)]
    for x in range(max(0, i - r), min(i + r + 1, r)):
        for y in range(max(0, j - c), min(j + c + 1, c)):
            if abs(i - x) + abs(j - y) <= n:
                result.append((x, y))
    return result



def suuji_basho():
    ans=[]
    for i in range(r):
        for j in range(c):
            if sheet[i][j].isdigit():
                ans.append([i,j,int(sheet[i][j])])
    return ans

suuji=suuji_basho()

for x,y,num in suuji:

    bakuhatu_place=manhattan_coordinates(x,y,num)
    for i,j in bakuhatu_place:
        sheet[i][j]="."

for i in sheet:
    print("".join(i))