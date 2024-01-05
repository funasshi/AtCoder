N, K = map(int, input().split())
S = input()

# K番目までoを通過、それ以外はxで埋める
T = ['x'] * N


# oの位置に予選を通過できる人がいるか探す
count=0
for i in range(N):
    if S[i] == 'o':
        T[i] = 'o'
        count+=1
    if count==K:
        break
print(''.join(T))
