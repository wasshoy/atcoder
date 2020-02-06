# https://atcoder.jp/contests/abc146/tasks/abc146_c
a, b, x = map(int, input().split())
ans =0
left = 0
right = 10**9+1

def dN(n):
  return len(str(n))

def cal_price(a, b, n):
  return a*n + b*dN(n)

while right - left > 1:
  mid = (left + right)//2
  if a*mid + b*dN(mid) > x: right = mid
  else: left = mid
    
print(left)