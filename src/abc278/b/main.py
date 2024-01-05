h, m = map(int, input().split())

# 時計の数字が入ったリスト
def next_time(h,m):
    if m==59:
        return (h+1)%24,0
    else:
        return h,m+1

def d(h,m):
    if h<10:
        d1='0'
        d2=str(h)
    else:
        d1=str(h)[0]
        d2=str(h)[1]
    if m<10:
        d3='0'
        d4=str(m)
    else:
        d3=str(m)[0]
        d4=str(m)[1]
    return d1,d2,d3,d4

# 見間違えやすい時刻を全て列挙

while True:
    d1,d2,d3,d4=d(h,m)
    swapped_h = int(str(d1) + str(d3))
    swapped_m = int(str(d2) + str(d4))
     # 入れ替えた時刻が存在する場合、見間違えやすい時刻の候補に加える
    if 0 <= swapped_h <= 23 and 0 <= swapped_m <= 59:
        break
    else:
        h,m=next_time(h,m)
# 見間違えやすい時刻の候補を時刻の早い順にソートし、最初に現れたものを出力

print(h,m)