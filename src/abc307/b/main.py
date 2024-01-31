# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


n = int(input())
s=[]

for i in range(n):
    s.append(input())
    
def is_kaibun(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[-i-1]:
            return False
    return True

flag=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if is_kaibun(s[i]+s[j]):
            flag=1

if flag==1:
    print("Yes")
else:
    print("No")

