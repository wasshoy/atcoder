# https://atcoder.jp/contests/abc152/tasks/abc152_c
n=int(input())
p=list(map(int, input().split()))

ans=1
minn=p[0]
for i in range(1,n):
  minn = min(p[i-1], minn)
  if minn >= p[i]: 
    ans+=1
print(ans)