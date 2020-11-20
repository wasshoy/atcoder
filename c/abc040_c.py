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


# 6m AC
n = I()
a = LI()
# dp[i] : i 本目の柱に移動するのにかかる最小コスト
dp = [INF] * (n+1)
dp[0] = 0
dp[1] = abs(a[1] - a[0])

for i in range(2, n):
    dp[i] = min(dp[i],
                dp[i-1] + abs(a[i] - a[i-1]),
                dp[i-2] + abs(a[i] - a[i-2]))
print(dp[n-1])
