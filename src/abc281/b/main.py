S = input()


def check():
    if len(S)!=8:
        return "No"
    if not S[0].isupper() or not S[7].isupper():
        return "No"
    try:
        num = int(S[1:7])
    except ValueError:
        return "No"
    if not (100000 <= num <= 999999):
        return "No"

    return "Yes"

print(check())