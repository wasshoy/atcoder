import sys
from collections import Counter


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')
MOD = 10**9 + 7
# 17
n = I()
s = S()
counter = Counter(s)
ans = 1
# Sの中で、 aが1個以下, bが1個以下, ..., zが1個以下 になるような部分文字列が条件を満たす
# ある文字 c の が x 回出現する場合 cが含まれる部分文字列のcの種類は、 1回目を選ぶ, 2回目を選ぶ, ..., x回目を選ぶ, cを選ばない の x+1 通りがある
for v in counter.values():
    ans *= v + 1
    ans %= MOD
ans -= 1  # どれも選ばない(=空文字列)の場合を除く
print(ans)
