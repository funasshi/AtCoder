n=int(input())


# ==================================================-
# modを考慮したべき乗
# a**n%modを高速に出力
def power_func(a, n, mod=10 ** 9 + 7):
    bi = str(format(n, "b"))
    res = 1
    for i in range(len(bi)):
        res = (res * res) % mod
        if bi[i] == "1":
            res = (res * a) % mod
    return res

mod=10**9+7
all_situation=power_func(10,n)

non_zero_situation=power_func(9,n)

non_nine_situation=power_func(9,n)

non_zero_and_nine_situation=power_func(8,n)

answer=(all_situation-non_zero_situation-non_nine_situation+non_zero_and_nine_situation)%mod
print(answer)