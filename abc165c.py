def return_d(A,abcds):
    sum_d=0
    for abcd in abcds:
        a,b,c,d=abcd
        if A[b]-A[a]==c:
            sum_d+=d
    return sum_d

n,m,q=[int(i) for i in input().split()]
abcds=[[int(i) for i in input().split()] for j in range(q)]


As=[]
for i_1 in range(1,m+1):
    for i_2 in range(i_1, m + 1):
        for i_3 in range(i_2, m + 1):
            for i_4 in range(i_3, m + 1):
                for i_5 in range(i_4, m + 1):
                    for i_6 in range(i_5, m + 1):
                        for i_7 in range(i_6, m + 1):
                            for i_8 in range(i_7, m + 1):
                                for i_9 in range(i_8, m + 1):
                                    for i_10 in range(i_9, m + 1):
                                        As.append([0,i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9,i_10])


ans=0
for A in As:
    ans=max(ans,return_d(A,abcds))

print(ans)