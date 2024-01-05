N = int(input())
S = input()

for i in range(1, N):
    ans_l=0
    for k in range(1,N-i+1):
        if S[k-1] == S[k+i-1]:
            break
        else:
            ans_l=k
    print(ans_l)
