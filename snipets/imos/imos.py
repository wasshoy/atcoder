# いもす法の素材
# いもす法 : n 個の要素を持つ配列に対し、ある区間への加算を行うクエリを q 回行うとき、
# 愚直にやると O(nq) かかるところを o(q + n) で実装できるようになる手法。
# 処理は 1. 加算処理(O(q)) と 累積和計算(O(n)) に分けられる


# 具体例
from virtual-con.abc035_c import cumsum


n = 7  # 要素数
q = 3  # クエリ数
query = [[1, 3, 2], [3, 3, 3], [0, 5, 1]]  # 区間[l, r] の要素に +v するというクエリ
a = [0] * n  # 配列の初期値 は 全て 0

# 1. 加算処理 : 区間[l, r] に +v => a[l]に +v, a[r + 1]に -v
for l, r, v in query:
    a[l] += v
    if r + 1 < n:
        a[r + 1] -= v


def calc_cumsum(l):
    cumsum = [0]
    for i in l:
        cumsum.append(cumsum[-1] + i)
    return cumsum


# 2. 累積和計算 : 加算処理を行った配列の累積和を計算 => 各要素の値がクエリを行った最終結果になる(すごい)
cumsum = calc_cumsum(a)[1:]
print(cumsum)
