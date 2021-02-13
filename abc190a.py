a, b, c = [int(i) for i in input().split()]

if c == 0:
    if a > b:
        print("Takahashi")
    else:
        print('Aoki')
else:
    if b > a:
        print("Aoki")
    else:
        print('Takahashi')
