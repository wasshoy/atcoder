# 6m AC
from collections import Counter
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


n, m = LI()
a = LI()
d = {k: v for k, v in Counter(a).items()}
ans = -1
for k, v in d.items():
    if v >= n // 2 + 1:
        ans = k
        break
if ans == -1:
    ans = '?'
print(ans)
