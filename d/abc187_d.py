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
MOD = 10**9 + 7

n = I()
a = []
b = []
sum_ab = []
for _ in range(n):
    ai, bi = LI()
    a.append(ai)
    b.append(bi)
    sum_ab.append(bi+2*ai)

sort_ab_i = np.argsort(sum_ab)[::-1]
ans = 0
diff = -sum(a)
for i in sort_ab_i:
    diff += b[i] + 2 * a[i]
    ans += 1
    if diff > 0:
        print(ans)
        exit()
