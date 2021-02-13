a, b, c, d = [int(i) for i in input().split()]

if a < c:
    sx, sy, gx, gy = a, b, c, d
else:
    gx, gy, sx, sy = a, b, c, d
print((sy*gx+sx*gy)/(gy+sy))
