n,m=[int(i) for i in input().split()]


class People:
    def __init__(self,name):
        self.friends= {name}

peoples=[People(i) for i in range(n+1)]

for i in range(m):
    a, b = [int(i) for i in input().split()]
    peoples[a].friends.add(b)
    peoples[b].friends.add(a)

for i in range(1,n+1):
    people=peoples[i]
    frends_of_frends=set()
    for friend in people.friends:
        frends_of_frends= frends_of_frends | (peoples[friend].friends-people.friends)
    print(len(frends_of_frends))
