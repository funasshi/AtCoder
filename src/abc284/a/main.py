n = int(input())
s_list = []
for i in range(n):
    s_list.append(input())
s_list = s_list[::-1]
for i in s_list:
    print(i)
