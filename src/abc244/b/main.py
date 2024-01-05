n = int(input())
t = input()

ans_list = []

moves = ["e", "s", "w", "n"]
move = 0
for command in t:
    if command == "S":
        ans_list.append(moves[move])
    else:
        move = (move+1) % 4

print(ans_list.count("e")-ans_list.count("w"),
      ans_list.count("n")-ans_list.count("s"))
