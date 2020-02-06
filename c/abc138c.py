# https://atcoder.jp/contests/abc138/tasks/abc138_c
n = int(input())
v = list(map(int, input().split()))
sort_v = sorted(v)
ans = sort_v[0]
for i in range(1, n):
  ans += (2**(i-1)) * sort_v[i]
ans /= 2**(n-1)
print(ans)