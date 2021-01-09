import sys
from collections import defaultdict


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


# 14m AC
n = I()
dd = defaultdict(int)  # 各素因数の個数


def prime_factrize_d(n):
    if n < 2:
        return
    # 2だけ先に取り分けておく
    while n % 2 == 0:
        dd[2] += 1
        n //= 2
    # 残りの奇数の素因数を探す
    f = 3
    while f * f <= n:
        if n % f == 0:
            dd[f] += 1
            n //= f
        else:
            f += 2
    # nが素数の場合
    if n != 1:
        dd[n] += 1


for i in range(2, n+1):
    prime_factrize_d(i)
ans = 1
for v in dd.values():
    ans *= v + 1
    ans %= MOD
print(ans)
