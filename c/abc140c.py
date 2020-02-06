# https://atcoder.jp/contests/abc140/tasks/abc140_c
n=int(input())
b=list(map(int, input().split()))
a=[0 for _ in range(n)]
a[0]=b[0]
a[n-1]=b[n-2]
for i in range(1, n-1):
  a[i]=min(b[i-1], b[i])
ans=sum(a)
print(ans)
