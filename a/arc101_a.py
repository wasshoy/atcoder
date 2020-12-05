import sys
import bisect


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 23
n, k = LI()
x = LI()
# 連続する k 本を選ぶのが最適
# 全探索 : n - k + 1 通り
ans = INF
for l in range(n-k+1):
    r = l + k - 1
    ans = min(ans,
              abs(x[l])+abs(x[r]-x[l]),
              abs(x[r])+abs(x[r]-x[l]))
print(ans)
