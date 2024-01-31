# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)

h,w=list(map(int,input().split()))
mapping=[]
for i in range(h):
    mapping.append(input())

def isValidIndex(x,y):
    if 0<=x<w and 0<=y<h:
        return True
    return False


for x in range(w):
    for y in range(h):
        if mapping[y][x]=="s":
            for dir_x,dir_y in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                if isValidIndex(x+4*dir_x,y+4*dir_y):
                    if mapping[y+dir_y][x+dir_x]=="n" and mapping[y+2*dir_y][x+2*dir_x]=="u" and mapping[y+3*dir_y][x+3*dir_x]=="k" and mapping[y+4*dir_y][x+4*dir_x]=="e":
                        print(y+1,x+1)
                        print(y+dir_y+1,x+dir_x+1)
                        print(y+2*dir_y+1,x+2*dir_x+1)
                        print(y+3*dir_y+1,x+3*dir_x+1)
                        print(y+4*dir_y+1,x+4*dir_x+1)
                        