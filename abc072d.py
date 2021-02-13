n = int(input())
p = [int(i) for i in input().split()]

haba_list = []

count = 0
for i, j in enumerate(p):
    if i+1 == j:
        count += 1
    elif count != 0:
        haba_list.append(count)
        count = 0
if count != 0:
    haba_list.append(count)


print(sum([(i+1)//2 for i in haba_list]))
