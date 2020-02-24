# https://atcoder.jp/contests/abc156/tasks/abc156_b
n,k = map(int, input().split())

def base(a, b):
  if (int(a/b)): return base(int(a/b), b) + str(a % b)
  return str(a % b)

ans = base(n, k)
print(len(ans))