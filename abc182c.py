n = input()
keta_list = [int(i) for i in list(n)]
k = len(keta_list)

amari_0 = 0
amari_1 = 0
amari_2 = 0

for keta in keta_list:
    if keta % 3 == 0:
        amari_0 += 1
    elif keta % 3 == 1:
        amari_1 += 1
    else:
        amari_2 += 1

if (amari_1+amari_2*2) % 3 == 0:
    ans = 0
elif amari_1 % 3 == 2 and amari_2 == 0:
    ans = 2
elif amari_2 % 3 == 2 and amari_1 == 0:
    ans = 2
else:
    ans = 1

if ans < k:
    print(ans)
else:
    print(-1)
