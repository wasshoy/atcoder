# 19分AC
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


n = I()
ans = float('inf')
root_n = int(math.sqrt(n))

for i in range(1, root_n + 1):
    j = n // i
    area = i * j
    tile_rest = n - area
    abso = abs(i - j)
    ans = min(ans, tile_rest + abso)

print(ans)
