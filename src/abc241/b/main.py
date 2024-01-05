n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()


def eat():
    for i in b[::-1]:
        flag = 0
        while flag == 0:
            men = a.pop()
            if men == i:
                flag = 1


try:
    eat()
except:
    print("No")
else:
    print("Yes")
