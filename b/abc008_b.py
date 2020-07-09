# 4m AC
from collections import defaultdict
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
n = I()
s = SR(n)
d = defaultdict(int)
for elem in s:
    d[elem] += 1
d = sorted(d.items(), key=lambda x: x[1])
print(d[-1][0])
