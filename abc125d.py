n = int(input())
a = list(map(int, input().split()))
count = 0
for num in a:
    if num < 0:
        count += 1
abs_a = [abs(i) for i in a]
if count % 2 == 0:
    print(sum(abs_a))
else:
    print(sum(abs_a)-2*min(abs_a))
