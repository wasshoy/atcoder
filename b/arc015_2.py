import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 10m AC
n = I()
d = {k: 0 for k in range(1, 7)}
for _ in range(n):
    max_t, min_t = map(float, input().split())
    if max_t >= 35:
        d[1] += 1
    elif max_t >= 30:
        d[2] += 1
    elif max_t >= 25:
        d[3] += 1

    if min_t >= 25:
        d[4] += 1

    if min_t < 0 and max_t >= 0:
        d[5] += 1

    if max_t < 0:
        d[6] += 1
d = sorted(d.items(), key=lambda x: x[0])
ans = [v[1] for v in d]
print(*ans, sep=' ')
