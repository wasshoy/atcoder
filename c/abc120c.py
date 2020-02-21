# https://atcoder.jp/contests/abc120/tasks/abc120_c
s = list(input())
n = len(s)
cntd = {'0':0, '1':0}

for i in range(n):
    cntd[s[i]] += 1
ans = 0
ans = 2 * min(cntd.values())
print(ans)