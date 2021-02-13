from scipy.special import comb
# a = comb(n, r)
l = int(input())
a = comb(l-1, 11, exact=True)
print(int(a))
