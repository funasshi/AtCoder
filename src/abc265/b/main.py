n, m, t = map(int, input().split())
a = list(map(int, input().split()))
bonus = [tuple(map(int, input().split())) for _ in range(m)]

room = 1
time = t

next_bonus_room=0
flag=0
for cost in a:
    if next_bonus_room<m:
        if room == bonus[next_bonus_room][0]:
            time +=bonus[next_bonus_room][1]
            next_bonus_room+=1

    time -=cost 
    if time <= 0:    
        flag=1
    room += 1

if flag==0:
    print("Yes")
else:
    print("No")