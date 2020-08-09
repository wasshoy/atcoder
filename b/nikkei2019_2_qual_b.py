# 7
from collections import Counter
import collections
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
d = LI()
mod = 998244353
if d[0] != 0:
    print(0)
    exit(0)

# 頂点 i に隣接する頂点のうち、頂点 1 に近い頂点を pi とすると
# d_pi = d_i - 1 となる
# 各 i (i >= 2) について上の条件を満たす pi の個数の総乗を求める
c = Counter(d)
counts = [0] * (max(d)+1)
for k, v in c.items():
    counts[k] = v
if counts[0] > 1:
    print(0)
    exit(0)
ans = 1
for i in range(1, len(counts)):
    ans *= pow(counts[i-1], counts[i])
    ans %= mod

print(ans)
