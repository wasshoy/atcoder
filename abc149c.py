# https://atcoder.jp/contests/abc149/tasks/abc149_c
x = int(input())
prim = x
flag = True

while(flag):
  if x==2:
    break
  for j in reversed(range(2, x)):
    if x % j == 0:
      #print('{} is not prime.'.format(x))
      flag = True
      break
    else:
      prim = x
      flag = False
  x += 1
print(prim)