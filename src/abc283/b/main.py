n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    query = input().split()
    if query[0] == '1':
        k = int(query[1]) - 1
        x = int(query[2])
        a[k] = x
    else:
        k = int(query[1]) - 1
        print(a[k])
