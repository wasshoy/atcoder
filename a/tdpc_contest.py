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

n = I()
p = [0] + LI()  # dpテーブルに合わせて 0 問目(=何も解答しない)を作成
# dp[i][j] : i 問目(1-indexed)までの問題を解答して 得点 j が可能かどうか
dp = [[False] * (sum(p)+1) for _ in range(n+1)]
dp[0][0] = True  # 0 点 は 何も解答しなくても可能
# 答え ： dp[n][j] = True となる要素の合計
for i in range(1, n+1):
    for j in range(sum(p)+1):
        if dp[i - 1][j]:
            # i-1問目までで既に条件を満たすなら、i問目まででも当然条件を満たす
            dp[i][j] = True
            dp[i][j + p[i]] = True  # j + p[i]点も条件を満たすことができる

ans = len([is_ok for is_ok in dp[n] if is_ok])
print(ans)
