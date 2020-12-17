import sys
import bisect


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

n, m = LI()
p = []
y = []
v = [[] for _ in range(n)]
for i in range(m):
    pi, yi = LI()
    p.append(pi)
    y.append(yi)
    pi -= 1
    v[pi].append(yi)

for i in range(n):
    v[i] = sorted(set(v[i]))

for i in range(m):
    pre = str(p[i]).zfill(6)
    pid = bisect.bisect_left(v[p[i]-1], y[i]) + 1
    pid = str(pid).zfill(6)
    print(pre + pid)
