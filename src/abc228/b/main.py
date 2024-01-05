n, x = list(map(int, input().split()))
a_list = list(map(int, input().split()))

know_list = [x]
for i in range(n):
    know_list.append(a_list[x-1])
    x = a_list[x-1]

print(len(set(know_list)))
