n, m = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ans = 0
for index in b_list:
    ans += a_list[index-1]
print(ans)
