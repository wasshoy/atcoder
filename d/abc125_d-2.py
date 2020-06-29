# DPで解く方法
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
a = LI()
# dp[i][j] : i を選んで ai と ai + 1 の符号を反転(j = 0 させない, j = 1 させる)場合の a1 + a2 + ... + ai-1 + ai の最大値
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 0  # dp[0] : 何も選んでいない（開始地点）
dp[0][1] = -float('inf')  # 定義されていないためすごい小さい値を入れる
for i in range(n):
    dp[i + 1][0] = max(dp[i][0] + a[i], dp[i][1] - a[i])  # i + 1を選んで反転させない
    dp[i + 1][1] = max(dp[i][0] - a[i], dp[i][1] + a[i])  # i + 1を選んで反転させる
print(dp[n][0])
