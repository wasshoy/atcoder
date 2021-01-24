import sys
from collections import Counter

sys.setrecursionlimit(10**7)


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
a = LI()
ans = 0
for l in range(n):
    x = a[l]
    for r in range(l, n):
        x = min(x, a[r])
        ans = max(ans, x*(r-l+1))
print(ans)
