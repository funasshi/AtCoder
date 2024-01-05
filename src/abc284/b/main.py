# 入力を受け取る
T = int(input())

# 各テストケースに対して処理を行う
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # 奇数の数を数える
    count = 0
    for a in A:
        if a % 2 == 1:
            count += 1

    # 結果を出力する
    print(count)

