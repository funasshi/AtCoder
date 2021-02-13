n=int(input())

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


points=[]

for i in range(n):
    x,y=[int(i) for i in input().split()]
    points.append(Point(x+y,x-y))

min_x=100000000000
max_x=-100000000000
min_y=100000000000
max_y=-100000000000

for point in points:
    if point.x<min_x:
        min_x=point.x
    if point.x>max_x:
        max_x=point.x
    if point.y<min_y:
        min_y=point.y
    if point.y>max_y:
        max_y=point.y

x_abs=max_x-min_x
y_abs=max_y-min_y
print(max(x_abs,y_abs))
