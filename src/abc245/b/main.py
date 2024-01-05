n = int(input())
a_list = list(map(int, input().split()))

i = 0
while i <= 2000:
    if i in a_list:
        i += 1
    else:
        print(i)
        break
