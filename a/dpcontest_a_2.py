# https://atcoder.jp/contests/dp/tasks/dp_a
import sys
n = int(sys.stdin.readline().strip('\n'))
h = list(map(int, sys.stdin.readline().strip('\n').split()))
dp = [float('inf') for _ in range(n)]
dp[0] = 0
for i in range(n):
  # 配るdp
  if i+1<=n-1: dp[i+1] = min(dp[i+1], dp[i] + abs(h[i]-h[i+1]))
  if i+2<=n-1: dp[i+2] = min(dp[i+2], dp[i] + abs(h[i]-h[i+2])) 
print(dp[n-1])
