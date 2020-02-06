# https://atcoder.jp/contests/abc141/tasks/abc141_c
n,k,q = map(int, input().split())
a = [int(input()) for i in range(q)]
win = [0 for _ in range(n)]
for ai in a:
  win[ai-1] += 1
for w in win:
  if k-q+w<=0: print('No')
  else: print('Yes')