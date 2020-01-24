# https://atcoder.jp/contests/abc152/tasks/abc152_b
a, b=input().split()
sa=''
sb=''
for i in range(int(b)):
  sa+=a
for i in range(int(a)):
  sb+=b
#print(sa, sb)
if sa < sb: print(sa)
else: print(sb)