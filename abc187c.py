n = int(input())

moji_list = []
for i in range(n):
    moji_list.append(input())

moji_remove_list = []
for moji in moji_list:
    if moji[0] == '!':
        moji_remove_list.append(moji[1:])

a = set(moji_list)
b = set(moji_remove_list)

c = a & b
if len(c) == 0:
    print('satisfiable')
else:
    print(c.pop())
