a, b = input().split()

a_sum = sum([int(i) for i in list(a)])
b_sum = sum([int(i) for i in list(b)])

if a_sum >= b_sum:
    print(a_sum)
else:
    print(b_sum)
