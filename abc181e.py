n, m = map(int, input().split())
students = list(map(int, input().split()))
students.sort()
hensin_heights = list(map(int, input().split()))
hensin_heights.sort()


min_sa = 0
for i, sintyou in enumerate(students):
    if i % 2 == 0:
        min_sa += sintyou
    else:
        min_sa -= sintyou

i = 0
now_sa = min_sa
flag = 0
for teature in hensin_heights:
    while teature > students[i]:
        if i % 2 == 0:
            now_sa -= 2*students[i]
        else:
            now_sa += 2*students[i]
        i += 1
        if i == n:
            flag = 1
            break
    if i % 2 == 0:
        now_sa -= teature
    else:
        now_sa += teature
    if now_sa < min_sa or teature == hensin_heights[0]:
        min_sa = now_sa
    if i % 2 == 0:
        now_sa += teature
    else:
        now_sa -= teature
    if flag == 1:
        break
print(min_sa)
