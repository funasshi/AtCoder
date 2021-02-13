import math
n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
white_widths = []

start = 0
for blue_position in a:
    white_width = blue_position-start-1
    if white_width != 0:
        white_widths.append(white_width)
    start = blue_position
if n != start:
    white_widths.append(n-start)


white_widths.sort()
if len(white_widths) == 0:
    print(0)
else:
    hanko_width = white_widths[0]
    count_list = [math.ceil(i/hanko_width) for i in white_widths]
    print(sum(count_list))
