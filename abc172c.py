# ==================================================-
# 二分探索
# functionを満たす,search_listの最大の要素を出力
# 【注意点】searchリストの初めの方はfunctionを満たし、後ろに行くにつれて満たさなくなるべき
import math
import sys

sys.setrecursionlimit(10 ** 9)


def binary_research(start, end,function):
    if start == end:
        return start
    middle = math.ceil((start + end) / 2)
    if function(middle, k, a_sum, b_sum):
        start = middle
    else:
        end = middle - 1
    return binary_research(start, end, function)


# ==================================================-

n, m, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a_sum = [0]
b_sum = [0]
for book in a:
    a_sum.append(a_sum[-1] + book)
for book in b:
    b_sum.append(b_sum[-1] + book)


def can_read(num, k, a_sum, b_sum):
    min_read_time = 1000000000000
    for i in range(max(0, num - m), min(num+1,n+1)):
        a_num = i
        b_num = num - i
        min_read_time = min(min_read_time, a_sum[a_num] + b_sum[b_num])
    if min_read_time <= k:
        return True
    return False


start = 0
end = n + m

print(binary_research(start, end, can_read))