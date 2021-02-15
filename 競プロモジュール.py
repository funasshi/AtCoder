
import functools
import sys
import math
import queue
import copy


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# modを考慮した組み合わせ
# nCrを高速に出力
# 上の２つが必要(egcd,modinv)
def combination(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res


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
# ==================================================-
# 深さ優先探索(BFS)による、上下左右移動可能な迷路の最短距離計算


# 再帰上限
sys.setrecursionlimit(10 ** 6)

# 最短距離メモ
# 0#4#
# 123
# 23#のような最終結果のためのメモ
# スタートからの最短距離が格納


def answer_sheet(meiro):
    return copy.deepcopy(meiro)


# 【周りの点の取得）
# 座標が与えられると、上下左右の4点を得る。
# 境界を超えた場合はカットされる。
def get_around_point(point, h, w):
    around_points = []

    for ij in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        i, j = ij
        new_i = point[0] + i
        new_j = point[1] + j
        if 0 <= new_i < h and 0 <= new_j < w:
            around_points.append([new_i, new_j])
    return around_points


# ある点が道かどうかを判別する
def walkable(point, meiro):
    i = point[0]
    j = point[1]
    if meiro[i][j] == ".":
        return True
    return False


# ある点が行ったことあるかどうか
def never_had_been(point, sheet):
    if sheet[point[0]][point[1]] == ".":
        return True
    else:
        return False


# キューに、ある点の周りの行ったことのない道を追加し、シートに距離を記入
def add_load_2_queue(point, h, w, meiro, sheet, que):
    around_points = get_around_point(point, h, w)
    for around_point in around_points:
        if walkable(around_point, meiro) and never_had_been(around_point, sheet):
            que.put(around_point)
            sheet[around_point[0]][around_point[1]
                                   ] = sheet[point[0]][point[1]] + 1
    return sheet, que


# ポイントが与えられたとき、その周りの道をキューに追加し、シートに記入、次のキューを取り出し同様の処理を行う。キューがなくなるまで続け、シートを返す。
def step(point, h, w, meiro, sheet, que):
    sheet, que = add_load_2_queue(point, h, w, meiro, sheet, que)
    if que.empty():
        return sheet
    next_point = que.get()
    return step(next_point, h, w, meiro, sheet, que)


# シートは、行けない場所の場合は"#"が含まれているため-1に変換
def hash2minus(sheet):
    new_sheet = []
    for gyou in sheet:
        new_gyou = []
        for item in gyou:
            if item == "#":
                new_gyou.append(-1)
            else:
                new_gyou.append(item)
        new_sheet.append(new_gyou)
    return new_sheet


# -------メイン関数---------
# スタートを決めた場合の、各場所までの最短距離を表すシートを出力
# 行けない場所の場合は-1
# 入力
# start 開始座標のリスト(例：[1,2])
# h 迷路の高さ
# w 迷路の幅
# meiro 迷路の文字列リスト
def min_dis(start, h, w, meiro):
    sheet = answer_sheet(meiro)
    que = queue.Queue()
    sheet[start[0]][start[1]] = 0
    return hash2minus(step(start, h, w, meiro, sheet, que))


# ==================================================-
# 二分探索
# functionを満たす,search_listの最大の要素を出力
# 【注意点】searchリストの初めの方はfunctionを満たし、後ろに行くにつれて満たさなくなるべき
sys.setrecursionlimit(10**9)


def binary_research(start, end, search_list, function):
    if start == end:
        return search_list[start]
    middle = math.ceil((start+end)/2)
    if function(search_list[middle]):
        start = middle
    else:
        end = middle-1
    return binary_research(start, end, search_list, function)

# ==================================================-
# n以下の数の約数の個数をリスト形式で全て出力


def number_of_divisor(n):
    ans = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            ans[j] += 1
    return ans

# ==================================================-
# n以下の数の約数をリスト形式で全て出力


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# ==================================================-
# 整数を２進数に変換
def get_conbination(i, length):
    return format(i, '#0'+str(length+2)+'b')[2:]


# ==================================================-
# 高速素因数分解
# """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

# ==================================================-
# 最大公約数n個


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


# ----メイン関数------------

# numsは整数のリスト
def gcd(nums):
    return functools.reduce(euclid, nums)


# ==================================================-
# 最大公約数n個
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def multiple(a, b):
    return a*b // euclid(a, b)


# ------メイン関数-------
# numsは整数のリスト


def lcm(nums):
    return functools.reduce(multiple, nums)


# ==================================================-
# modありの階乗
def kaijyou(n, mod):
    ans = 1
    for i in range(1, n+1):
        ans *= i
        ans = ans % mod
    return ans

# ==================================================-
# セグメント木


def segfunc(x, y):
    # ここに計算したいことを書く
    return
#################


#####単位元を定める#####
ide_ele =
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値 (要素の数は2のべき乗でなくても、自動で揃えてくれる)
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
