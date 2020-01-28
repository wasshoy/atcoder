# https://atcoder.jp/contests/dp/tasks/dp_a
import sys
n = int(sys.stdin.readline().strip('\n'))
h = list(map(int, sys.stdin.readline().strip('\n').split()))
dp = [float('inf') for _ in range(n)]
dp[0] = 0
dp[1] = abs(h[0]-h[1])
for i in range(2, n):
  # 集めるdp
  dp[i] = min(dp[i-1] + abs(h[i-1]-h[i]), 
             dp[i-2] + abs(h[i-2]-h[i]))
print(dp[n-1])
