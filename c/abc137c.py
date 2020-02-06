# https://atcoder.jp/contests/abc137/tasks/abc137_c
from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
cnt = 0
d = {}
for i in range(n):
  # アルファベット順にソート 
  sortsi = ''.join(sorted(s[i]))
  # 同じ並びの文字列があればカウントを足す
  if sortsi in d:
    cnt+=d[sortsi]
    # 既に存在した同じ並びの文字列とのペア数分を足す
    d[sortsi]+=1
  else: 
    d[sortsi]=1
print(cnt)