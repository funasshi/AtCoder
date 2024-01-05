S = input().strip()
T = input().strip()

n = len(S)
m = len(T)

# T が S の部分文字列であるかを調べる
for i in range(n - m + 1):
    if S[i:i + m] == T:
        print("Yes")
        exit()

print("No")
