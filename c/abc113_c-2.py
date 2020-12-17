import sys
import numpy as np
from collections import defaultdict


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 15
n, m = LI()
p = []
y = []
for _ in range(m):
    pi, yi = LI()
    p.append(pi)
    y.append(yi)

sort_y_inds = np.argsort(y)

dd = defaultdict(int)
res = []
for i in sort_y_inds:
    x = str(p[i]).zfill(6) + str(dd[p[i]]+1).zfill(6)
    dd[p[i]] += 1
    res.append([i, x])
ans = sorted(res, key=lambda x: x[0])  # 元の順番にソート
for _, pid in ans:
    print(pid)
