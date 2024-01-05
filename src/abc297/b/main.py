s = input()
def my_index_multi(l, x):
    a=[i for i, _x in enumerate(l) if _x == x]
    a.sort()
    return a

def b():
    one,two=my_index_multi(s,'B')
    if (one+two)%2==1:
        return True
    return False


def kr():
    k=my_index_multi(s,'K')[0]
    r_one,r_two=my_index_multi(s,'R')
    if r_one<k<r_two:
        return True
    return False

if b() and kr():
    print("Yes")
else:
    print("No")