# https://atcoder.jp/contests/abc142/tasks/abc142_c
n = int(input())
a = list(map(int, input().split()))
ans = [0 for _ in range(n)]
for i in range(n):
  ans[a[i]-1] = i + 1
for i in ans:
  print(i, end=' ')