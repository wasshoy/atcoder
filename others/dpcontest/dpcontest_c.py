# https://atcoder.jp/contests/dp/tasks/dp_c
import sys
n = int(sys.stdin.readline().strip('\n'))
a = [list(map(int, sys.stdin.readline().strip('\n').split())) for _ in range(n)]
# dp[i+1][j]: i日目までの活動に加え、i+1日目に活動jを選んだときの幸福度の最大値
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(n):
  for j in range(3):
    for k in range(3):
      if j==k: continue
      dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i][k])
#for i in range(n+1): print(dp[i])
print(max(dp[n]))