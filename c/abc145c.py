# https://atcoder.jp/contests/abc145/tasks/abc145_c
import math
n = int(input())
c = [list(map(int, input().split())) for i in range(n)]
#print(n)
#print(c)
def euc_dist(c1, c2):
  x1, y1 = c1
  x2, y2 = c2
  return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 10)

d = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
  for j in range(n):
    if i==j: d[i][j] = 0
    else: d[i][j] = euc_dist(c[i], c[j])
#print(d)

sum = 0
for i in range(n):
  for j in range(n):
    #print('sum={}'.format(sum))
    sum += d[i][j]
#print('sum={}, (n-1)!={}, n={}'.format(sum, math.factorial(n-1), n))
print(sum/n)