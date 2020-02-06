# https://atcoder.jp/contests/abc151/tasks/abc151_c
n,k,m = map(int,input().split())
a = list(map(int, input().split()))
ans=0
sum=0
for i in a:
  sum+=i
t=n*m - sum
if t>k:
  ans=-1
else: 
  if t>0: ans=t
  else: ans=0
print(ans)