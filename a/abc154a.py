# https://atcoder.jp/contests/abc154/tasks/abc154_a
s, t = input().split()
a, b = map(int, input().split())
u = input()
if u == s: a -= 1
else: b -= 1
print(a, b)