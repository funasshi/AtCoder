import math
x, y, r = [float(i) for i in input().split()]
min_y_int = math.ceil(y-r)
max_y_int = math.floor(y + r)


def x_hit_point(y_check):
    d = r ** 2-(y - y_check)**2
    if d >= 0:
        one = math.ceil(x - d ** 0.5)
        two = math.floor(x + d ** 0.5)
        if two >= one:
            return int(two - one + 1)
        else:
            return 0
    else:
        return 0


ans = 0
for y_check in range(min_y_int, max_y_int + 1):
    ans += x_hit_point(y_check)
print(ans)
