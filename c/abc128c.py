# https://atcoder.jp/contests/abc128/tasks/abc128_c
n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

s = []
ans = 0
for i in range(m):
  k = ks[i][0]
  l = [ks[i][j] for j in range(1, k+1)]
  s.append(l)

swh = [False for _ in range(n)]
for i in range(2 ** n):
  #print('######')
  flag = True
  # スイッチの状態
  for j in range(n):
    if ((i >> j) & 1): swh[j] = True
    else: swh[j] = False
      
  # 現在の状態での各電球の点灯をチェック    
  for j in range(m):
      #print('電球{}'.format(j))
      judge = [swh[si-1] for si in s[j]]
      #print(judge)
      if judge.count(True) % 2 != p[j]:
        flag = False
        break
        
  if flag: ans += 1
  #print('ans = {}'.format(ans))
      
print(ans)