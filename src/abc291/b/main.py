n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(x)

# 高橋君の得点を計算
score = sum(x_sort[n:4*n]) / (3*n)

print(score)
