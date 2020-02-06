# https://atcoder.jp/contests/abc133/tasks/abc133_c
l, r = map(int, input().split())
mod = 2019

def check(left, right):
  ans = 2018
  # a mod p = b mod p なら a*c ≡ b*c (mod p)
  # なので、iかjどちらかが2019で割り切れれば答えは0になる
  # 余りが2019種類あるなら余りの最小値は0
  if right-left >= 2019:
    ans = 0
# leftとrightが近い場合
  else:
# 2018**2個調べる(余りの最小値0が出たら打ち切り)
# 2018**2 = 4,072,324 なので間に合う
    for i in range(left, right):
      for j in range(l+1, right+1):
        ans = min((i*j)%mod, ans)
        if ans==0: return ans
  return ans
ans = check(l, r)
print(ans)
