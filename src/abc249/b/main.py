s = input()

is_contain_upper = len(set(list(s.upper())) & set(list(s))) > 0
is_contain_lower = len(set(list(s.lower())) & set(list(s))) > 0
is_barabara = (len(list(s)) == len(set(list(s))))

if is_barabara and is_contain_lower and is_contain_upper:
    print("Yes")
else:
    print("No")
