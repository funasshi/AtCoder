from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))

counter = Counter(a)

for i in range(m):
    b, c = map(int, input().split())
    counter[c] += b
h = counter.items()
sorted_count = sorted(counter.items(), key=lambda x: x[0], reverse=True)


pic_count = 0
sum_ = 0
for item in sorted_count:
    number, count = item
    if pic_count+count > n:
        sum_ += (n-pic_count)*number
        pic_count = n
    else:
        sum_ += count*number
        pic_count += count
    if pic_count == n:
        break
print(sum_)
