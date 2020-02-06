# https://atcoder.jp/contests/abc153/tasks/abc153_b
h, n = map(int, input().split())
a = list(map(int, input().split()))
for ai in a:
  h -= ai
judge = 'Yes' if h <= 0 else 'No'
print(judge)