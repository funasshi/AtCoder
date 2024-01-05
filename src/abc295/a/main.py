n = int(input())
w_list=input().split()

kouho=["and", "not", "that", "the", "you"]

if len(set(w_list) & set(kouho))==0:
    print("No")
else:
    print("Yes")