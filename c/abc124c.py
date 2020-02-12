# https://atcoder.jp/contests/abc124/tasks/abc124_c
import sys
s = list(sys.stdin.readline())
n = len(s)
ans = 0
for i in range(n-1):
    if s[i] != s[i+1]: continue
    if s[i] == '0': s[i+1] = '1'
    else: s[i+1] = '0'
    ans += 1
print(ans)
