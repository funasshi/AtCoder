# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
s=input()

if 'o' in s and 'x' not in s:
    print("Yes")
else:
    print("No")