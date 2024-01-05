import copy
n = int(input())
myouji_list = []
name_list = []

for i in range(n):
    myouji, name = input().split()
    myouji_list.append(myouji)
    name_list.append(name)

flag = 0
for i in range(n):
    tmp_myouji = copy.copy(myouji_list)
    del tmp_myouji[i]
    tmp_name = copy.copy(name_list)
    del tmp_name[i]
    kouho = tmp_name+tmp_myouji
    if myouji_list[i] in kouho and name_list[i] in kouho:
        flag = 1

if flag == 0:
    print("Yes")
else:
    print("No")
