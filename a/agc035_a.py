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


n = I()
a = LI()
# 条件を満たす状態における 連続する 4 つの値に関して考えると
# a_i = a_(i+3) を満たす事がわかる
# 満たす条件は
# a1 ^ a2 ^ a3 = 0
# a_i = a_(i+3) -> 値が 3 種類以内
c = Counter(a)
n_uniq = len(c)
# 値が 3 種類以上であれば No
if n_uniq > 3:
    print('No')
#  a1, a2, a3 の場合分けを考える
# 3 種類の異なる値の場合 : a1, a2, a3 が n 枚のうちちょうど同じ数ずつある必要がある (-> n / 3 が 3 の倍数)
elif n_uniq == 3:
    a_1, a_2, a_3 = c.keys()
    if a_1 ^ a_2 ^ a_3 == 0 and c[a_1] == c[a_2] == c[a_3]:
        print('Yes')
    else:
        print('No')
# 2 種類の異なる値の場合 : ある 1 つの値が必ず 0 -> 0 が n / 3 枚、 等しい数となる a_x は 2n / 3 枚
elif n_uniq == 2:
    a_1, a_2 = sorted(set(a))
    if a_1 == 0 and 3 * c[a_1] == n:
        print('Yes')
    else:
        print('No')
# 全て同じ値の場合 : 全て 0
else:
    if sum(a) == 0:
        print('Yes')
    else:
        print('No')
