# ランレングス圧縮の考え方で解く
# 自分の回答より 1.5 倍くらい早い
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 初期位置が R の人が最終的にどこに向かうかを考える
# 折り返し地点(移動中に訪れる初めての L) までの距離 d と操作回数の偶奇で決まる(今回の操作回数は偶数)
# d が奇数のとき 折り返し地点の 1 つ左側
# d が偶数のとき 折り返し地点
# L も同様に考える
# 折り返し地点(移動中に訪れる初めての R) までの距離 d と操作回数の偶奇で決まる(今回の操作回数は偶数)
# d が奇数のとき 折り返し地点
# d が偶数のとき 折り返し地点の 1 つ右側

# 連続する R と L をそれぞれグループ化することで折り返し地点を管理しやすくなる
# ランレングス圧縮と同じ


s = S()
n = len(s)
ans = [0] * n
# 初期位置が R の人について
# まとまりの人数、 その中で d が偶数の人の数、 d が奇数の人の数 を計算
r_cnt = 0
for i in range(n):
    if s[i] == 'R':
        r_cnt += 1
    else:  # 折り返し地点に来たら計算
        even_num = r_cnt // 2
        odd_num = r_cnt - even_num
        ans[i] += even_num  # 折り返し地点の人数
        ans[i - 1] += odd_num  # 折り返し地点の １ つ左の人数
        r_cnt = 0

# 初期位置が L の人について
# まとまりの人数、 その中で d が偶数の人の数、 d が奇数の人の数 を計算
l_cnt = 0
for i in range(n - 1, -1, -1):  # 右側から見ていく
    if s[i] == 'L':
        l_cnt += 1
    else:  # 折り返し地点に来たら計算
        even_num = l_cnt // 2
        odd_num = l_cnt - even_num
        ans[i] += even_num  # 折り返し地点の人数
        ans[i + 1] += odd_num  # 折り返し地点の １ つ右の人数
        l_cnt = 0
print(*ans)
