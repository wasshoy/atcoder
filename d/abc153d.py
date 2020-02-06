# https://atcoder.jp/contests/abc153/tasks/abc153_d
h = int(input())
def battle(x):
    if x==1: return 1
    else:
      return 1 + 2 * battle(x//2)
ans = battle(h)
print(ans)