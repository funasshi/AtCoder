n = int(input())
strings = set()
for i in range(n):
    s = input()
    if s[0] not in ['H', 'D', 'C', 'S'] or s[1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        print('No')
        break
    if s in strings:
        print('No')
        break
    strings.add(s)
else:
    print('Yes')
