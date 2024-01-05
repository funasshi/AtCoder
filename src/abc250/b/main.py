n, a, b = list(map(int, input().split()))

kirikae = 0
moto_white = "."*b
moto_black = "#"*b

motos = [moto_white, moto_black]

for i in range(a*n):
    kansei = ""
    for j in range(n):
        kansei = kansei+motos[(kirikae+j) % 2]
    print(kansei)
    if i % a == a-1:
        kirikae = (kirikae+1) % 2
