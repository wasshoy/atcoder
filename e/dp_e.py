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


n, W = LI()
w = []
v = []

for _ in range(n):
    wi, vi = LI()
    w.append(wi)
    v.append(vi)

# dp[i+1][j] : i (i=1, ...)番目の品物まで選べ、価値が j になるような場合の重さの最小値
max_v = sum(v) + 10
dp = [[INF] * (max_v+1) for _ in range(n+1)]
# 答え : dp[n][v] <= W 以下である v の中の最大値
dp[0][0] = 0  # 選べる荷物がない状態で 価値 0 を満たすとき、何も選ばないので重さは 0
for i in range(n):
    for sum_v in range(max_v):
        if sum_v - v[i] >= 0:
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v - v[i]] + w[i])
        dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])

ans = 0
for sum_v in range(max_v):
    if dp[n][sum_v] <= W:
        ans = sum_v

print(ans)
