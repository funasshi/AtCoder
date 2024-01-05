n, k = list(map(int, input().split()))
food_list = [(i+1, int(taste))
             for i, taste in enumerate(input().split())]
hate_list = list(map(int, input().split()))


def select_most_yummy_food_index(food_list):
    return [i for i, taste in food_list if taste == max(food_list, key=lambda x:x[1])[1]]


def check_hate_food(yummy_food_index):
    for index in yummy_food_index:
        if index in hate_list:
            return True
    return False


if check_hate_food(select_most_yummy_food_index(food_list)):
    print("Yes")
else:
    print("No")
