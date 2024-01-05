x, y, z = map(int, input().split())

def hantei():
    if (0<y<x and y<z) or (x<y<0 and z<y):
        return -1
    elif (0<y<x and z<y) or (x<y<0 and y<z):
        if z*x<0:
            return 2*abs(z)+abs(x)
        else:
            return abs(x)
    else:
        return abs(x)

print(hantei())

