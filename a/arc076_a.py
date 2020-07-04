# 30?m AC
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
MOD = 10 ** 9 + 7


n, m = LI()
if abs(n - m) > 1:
    print(0)
    sys.exit()

ans = 1
for i in range(1, n + 1):
    ans = ans * i % MOD
for i in range(1, m + 1):
    ans = ans * i % MOD
if n == m:
    ans = ans * 2 % MOD
print(ans % MOD)
