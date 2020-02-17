# https://atcoder.jp/contests/abc155/tasks/abc155_c
n = int(input())
s = [input() for _ in range(n)]
d = {}
for w in s:
    if w not in d:
        d[w] = 0
    d[w] += 1
d2 = sorted(d.items(), key=lambda x:x[1], reverse=True)
maxcnts = [w[0] for w in d2 if w[1] == d2[0][1]]
maxcnts.sort()
for ans in maxcnts:
    print(ans)