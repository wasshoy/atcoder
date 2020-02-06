# https://atcoder.jp/contests/abc143/tasks/abc143_c
n = int(input())
s = input()
ans = 1
for i in range(len(s)-1):
  if s[i]==s[i+1]:
    continue
  else:
    ans += 1
print(ans)