n = int(input())
a_list = list(map(int, input().split()))
gusuu=[i for i in a_list if i%2==0]
print(*gusuu)
