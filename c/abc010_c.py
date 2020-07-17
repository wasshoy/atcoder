# 11m AC
import math
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

tx_a, ty_a, tx_b, ty_b, t, v = LI()
n = I()
ans = 'NO'
for _ in range(n):
    x, y = LI()
    d = math.sqrt(pow((tx_a - x), 2) + pow(ty_a - y, 2)) \
        + math.sqrt(pow(x - tx_b, 2) + pow(y - ty_b, 2))
    if d <= t * v:
        ans = 'YES'
        break
print(ans)
