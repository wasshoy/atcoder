import sys
from itertools import permutations


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 43
n, m, l = LI()
nimotsu = LI()
ans = 0
# 箱の各辺に荷物の各辺を割り当てる
for i, j, k in permutations([i for i in range(3)]):
    ans = max(ans, (n//nimotsu[i]) * (m//nimotsu[j]) * (l//nimotsu[k]))
print(ans)
