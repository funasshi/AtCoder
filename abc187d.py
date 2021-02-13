n = int(input())

a_list = []
b_list = []
plus_sa = []

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    a_list.append(a)
    b_list.append(b)
    plus_sa.append(2*a+b)

sa = sum(a_list)

plus_sa.sort(reverse=True)

ans = 0
while sa >= 0:
    sa -= plus_sa[ans]
    ans += 1
print(ans)
