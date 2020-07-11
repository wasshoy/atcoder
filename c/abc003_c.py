# 13AC 1WA
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
r = LI()
ans = 0
r = sorted(r)[::-1][:k][::-1]
for i in range(k):
    ans += r[i] / 2 ** (k - i)
print(ans)
