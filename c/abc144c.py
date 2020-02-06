# https://atcoder.jp/contests/abc144/tasks/abc144_c
import math
n = int(input())
root = int(math.sqrt(n))
ans = 0
for i in range(1, root+1):
  if n % i == 0:
    ans = int((n/i)) + i - 2
print(ans)