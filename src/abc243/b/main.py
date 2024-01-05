n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ans_1 = 0

for i in range(n):
    if a_list[i] == b_list[i]:
        ans_1 += 1

print(ans_1)

ans_2 = 0


print(len(set(a_list) & set(b_list))-ans_1)
