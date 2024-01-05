n = int(input())
point_list = []
for i in range(n):
    point_list.append(list(map(int, input().split())))

len_list = []

for i in range(n-1):
    for j in range(i, n):
        x_1, y_1 = point_list[i]
        x_2, y_2 = point_list[j]
        len_list.append(((x_1-x_2)**2+(y_1-y_2)**2)**0.5)
print(max(len_list))
