# https://atcoder.jp/contests/abc152/tasks/abc152_d
n=int(input())
cnt=0
# c(i,j)={先頭がiで末尾がjであるkの個数}
c=[[0 for _ in range(10)] for _ in range(10)]
for i in range(1,n+1):
  l=int(str(i)[0])
  r=int(str(i)[-1])
  c[l][r]+=1
'''
for i in range(10):
  for j in range(10):
    print(c[i][j], end=' ')
  print('')
'''
sum=0
for i in range(1,10):
  for j in range(1,10):
    sum+=c[i][j]*c[j][i]
print(sum)