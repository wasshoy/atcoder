# https://atcoder.jp/contests/abc153/tasks/abc153_b
h, n = map(int, input().split())
a = list(map(int, input().split()))
judge = 'No'
for ai in a:
  h -= ai
if h <= 0: judge = 'Yes'
print(judge)