import sys
import math


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


n, d = LI()
ans = 0
for _ in range(n):
    x, y = LI()
    if x ** 2 + y ** 2 <= d ** 2:
        ans += 1
print(ans)
