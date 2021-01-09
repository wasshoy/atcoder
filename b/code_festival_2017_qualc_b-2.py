import sys
from functools import reduce
from itertools import product
from operator import mul


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 別解：より早い解法（解説の解法）
n = I()
a = LI()
ans = 0
even_num = 0
for ai in a:
    if ai % 2 == 0:
        even_num += 1
# 全ての要素が奇数となるような数列 bを考える
# a_i が偶数のとき b_i = a_i - 1 または a_i + 1 (2パターン)
# a_i が奇数のとき b_i = a_i (1パターン)
# よって 2^(偶数であるa_iの個数) * 1 パターンは全ての要素が奇数
ans = 3**n - 2**even_num
print(ans)
