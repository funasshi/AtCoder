n, x, y, z = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

jyukennsei_list = []


for i in range(n):
    jyukennsei_list.append([i, a_list[i], b_list[i], a_list[i]+b_list[i]])

goukaku = []

# 数学
jyukennsei_list.sort(key=lambda x: (x[1], -x[0]))

for i in range(x):
    jyukensei = jyukennsei_list.pop()
    goukaku.append(jyukensei[0])


# 英語
jyukennsei_list.sort(key=lambda x: (x[2], -x[0]))

for i in range(y):
    jyukensei = jyukennsei_list.pop()
    goukaku.append(jyukensei[0])
# 英語+数学
jyukennsei_list.sort(key=lambda x: (x[3], -x[0]))

for i in range(z):
    jyukensei = jyukennsei_list.pop()
    goukaku.append(jyukensei[0])

goukaku.sort()

for i in goukaku:
    print(i+1)
