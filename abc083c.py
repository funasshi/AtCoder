x,y=[int(i) for i in input().split()]


def func(i):
    return len(bin(i))-2

print(func(y//x))