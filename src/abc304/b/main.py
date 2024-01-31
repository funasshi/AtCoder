# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())

if n<1000:
    print(n)
elif n<10000:
    print(str(n)[:-1]+"0")
elif n<100000:
    print(str(n)[:-2]+"00")
elif n<1000000:
    print(str(n)[:-3]+"000")
elif n<10000000:
    print(str(n)[:-4]+"0000")
elif n<100000000:
    print(str(n)[:-5]+"00000")
elif n<1000000000:
    print(str(n)[:-6]+"000000")