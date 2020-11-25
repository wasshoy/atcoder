import sys
from itertools import combinations


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
g = [[False] * n for _ in range(n)]
for _ in range(m):
    xi, yi = LI()
    xi -= 1
    yi -= 1
    g[xi][yi] = True
    g[yi][xi] = False

ans = 0
for i in range(2**n):
    selected = [j for j in range(n) if i >> j & 1 == 1]
    is_ok = True
    for a, b in combinations(selected, 2):
        if not(g[a][b]):
            is_ok = False
            break
    if is_ok:
        ans = max(ans, len(selected))
print(ans)
