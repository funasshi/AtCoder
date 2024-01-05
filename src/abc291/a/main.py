s = input()


def f():
    for i, char in enumerate(s):
        if char.isupper():
            return i+1


print(f())
