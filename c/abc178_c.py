import sys
from scipy.special import comb


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

n = I()
ans = pow(10, n) % MOD
ans = (ans - pow(9, n)) % MOD
ans = (ans - pow(9, n)) % MOD
ans = (ans + pow(8, n)) % MOD
print(ans)
