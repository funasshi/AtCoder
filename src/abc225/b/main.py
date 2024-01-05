n = int(input())

hen = []
for i in range(n-1):
    hen.append(list(map(int, input().split())))

# 頂点を検索
kouho1 = hen[0][0]
kouho2 = hen[0][1]

if kouho1 == hen[1][0] or kouho1 == hen[1][1]:
    tyouten = kouho1
else:
    tyouten = kouho2

ko = [tyouten]
for a, b in hen:
    if a == tyouten:
        ko.append(b)
    else:
        ko.append(a)

ko.sort()

if len(set(ko)) == n:
    print("Yes")
else:
    print("No")
