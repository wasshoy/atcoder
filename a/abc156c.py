# https://atcoder.jp/contests/abc156/tasks/abc156_a
n,r = map(int, input().split())
ans = r
if n < 10: ans = r + 100 * (10 - n)
print(ans)