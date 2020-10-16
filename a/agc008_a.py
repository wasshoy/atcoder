import sys
import numpy as np


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

x, y = LI()
ans = 0
if x <= y:
    if np.sign(x*y) >= 0:
        ans = abs(y - x)
    else:
        if abs(x) <= abs(y):
            ans = y + x + (0 if x == 0 or y == 0 else 1)
        else:
            ans = abs(y + x) + (0 if x == 0 or y == 0 else 1)
elif x > y:
    if np.sign(x*y) >= 0:
        ans = abs(y - x) + (1 if x == 0 or y == 0 else 2)
    else:
        if abs(x) >= abs(y):
            ans = x + y + 1
        else:
            ans = abs(y) - x + 1
print(ans)
