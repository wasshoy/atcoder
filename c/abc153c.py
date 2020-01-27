# https://atcoder.jp/contests/abc153/tasks/abc153_c
n, k = map(int, input().split())
h = list(map(int, input().split()))
h = sorted(h, reverse=True)
ans = 0
if len(h) >= k:
  for i in range(k):
    h[i] = 0
  ans = sum(h) + 0
print(ans)