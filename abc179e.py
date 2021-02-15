n, x, m = map(int, input().split())

visited = [False]*m
ans_list = [x]
visited[x] = True
count = 1
while count < n:
    next_number = ans_list[-1]**2 % m
    if visited[next_number]:
        break
    else:
        visited[next_number] = True
        ans_list.append(next_number)
        count += 1


if count == n:
    print(sum(ans_list))
else:
    index = ans_list.index(next_number)
    pre = ans_list[:index]
    post = ans_list[index:]
    num1 = len(pre)
    num2 = len(post)
    remain_num = n-num1
    roop_count = remain_num//num2
    deppari_count = remain_num-roop_count*num2
    print(sum(pre)+roop_count*sum(post)+sum(post[:deppari_count]))
