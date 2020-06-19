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


n = I()
a = IR(n)
c = Counter(a)
ans = 0
for k, v in c.items():
    if v > 1:
        ans += v - 1
print(ans)
