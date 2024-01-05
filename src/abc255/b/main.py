n, c = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = [i for i in range(1, n+1) if i not in a_list]
zahyou = []
for i in range(n):
    zahyou.append(list(map(int, input().split())))


def kyori(i, j):
    one = zahyou[i-1]
    two = zahyou[j-1]
    return ((one[0]-two[0])**2+(one[1]-two[1])**2)**0.5


ans2 = []

for mottenaihito in b_list:
    ans = []
    for motteruhito in a_list:
        ans.append(kyori(mottenaihito, motteruhito))
    ans2.append(min(ans))

print(max(ans2))
