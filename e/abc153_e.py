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
# 50
sys.setrecursionlimit(10**7)

h, n = LI()
a = []
b = []
for _ in range(n):
    ai, bi = LI()
    a.append(ai)
    b.append(bi)
# dp[i+1][j] : 魔法 i(=1, 2,...) までを 0回以上使用できるとき、体力 j を 0にするのに消耗する魔力の最小値(i は 1-origin なので i = 0 は魔法を何も使わない場合)
dp = [[INF] * (h+1) for _ in range(n+1)]
dp[0][0] = 0  # 魔法を使わない
for i in range(n):
    for j in range(h+1):
        if j <= a[i]:
            # min(魔法 i を使わない(dp表の真上をスライド), 魔法 i を使う)
            dp[i+1][j] = min(dp[i][j], b[i])
        else:
            # min(魔法 i を使わない(dp表の真上をスライド), 魔法 i をもう一回使う)
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-a[i]] + b[i])
print(dp[n][h])
