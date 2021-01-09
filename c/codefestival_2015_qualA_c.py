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

# 22m AC
n, t = LI()
a = []
b = []
for _ in range(n):
    ai, bi = LI()
    a.append(ai)
    b.append(bi)

time = sum(a)
if time <= t:
    print(0)
    exit()

if sum(b) > t:
    print(-1)
    exit()

diff = [ai - bi for ai, bi in zip(a, b)]
sort_d_ind = np.argsort(diff)[::-1]

ans = 0
for i in sort_d_ind:
    time -= diff[i]
    ans += 1
    if time <= t:
        break
print(ans)
