n = int(input())

and_ors = [input() for i in range(n)]

count = 0

true = [1]
false = [1]

for ox in and_ors:
    if ox == 'AND':
        true.append(true[-1])
        false.append(true[-1]+2*false[-1])
    else:
        true.append(2*true[-1]+false[-1])
        false.append(false[-1])
print(true[-1])
