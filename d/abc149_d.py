
from collections import Counter
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


n, k = LI()
r, s, p = LI()
d = {'r': p, 's': r, 'p': s}
t = S()
ans = 0

# 結果が干渉し合うのは k = 4 とすると
# 1, 5, 9, ...
# 2, 6, 10, ...
# 3, 7, ...
# 4, 8, ...
# となり、各グループごとに独立に考えていい
# それぞれのグループで「連続して同じ手がだせない」じゃんけんをする
# 貪欲法 での解法
for j in range(k):
    is_win_last = False  # 前回勝ったかかどうか
    i = j
    while i < n:
        # 前回と手が同じで、前回は勝っている場合
        if i >= k and t[i - k] == t[i] and is_win_last:
            is_win_last = False
        else:  # 前回と手が異なる場合 もしくは 前回と手が同じだが負けている場合
            ans += d[t[i]]
            is_win_last = True
        i += k


print(ans)
