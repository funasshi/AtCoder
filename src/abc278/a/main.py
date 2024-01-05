n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))

ans = a_list[k:]+[0] * k
print(*ans[:n])
