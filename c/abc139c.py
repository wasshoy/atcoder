# https://atcoder.jp/contests/abc139/tasks/abc139_c
n = int(input())
h = list(map(int, input().split()))
l = []
cnt = 0
ans = 0
for i in reversed(range(1, n)):
  if h[i]<=h[i-1]:
    cnt += 1
  else:
    l.append(cnt)
    cnt = 0
  if i==1:
    l.append(cnt)

if len(l)!=0: ans = max(l)
print(ans)