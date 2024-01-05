n = int(input())
a_list = list(map(int, input().split()))

max_value = max(a_list)
max_index = a_list.index(max_value)

print(1+max_index)
