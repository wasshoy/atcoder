# https://atcoder.jp/contests/dp/tasks/dp_b
# pythonでTLE, pypy3でAC
import sys
n, k = map(int, sys.stdin.readline().strip('\n').split())
h = list(map(int, sys.stdin.readline().strip('\n').split()))
dp = [float('inf') for _ in range(n)]
dp[0] = 0
for i in range(1, n):
  for j in range(k+1):
    # 集めるdp
    if i-j>=0: dp[i] = min(dp[i], dp[i-j] + abs(h[i-j]-h[i]))
print(dp[n-1])
