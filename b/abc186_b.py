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

h, w = LI()
a = LIR(h)
min_a = INF
for i in range(h):
    for j in range(w):
        min_a = min(min_a, a[i][j])


ans = 0
for i in range(h):
    for j in range(w):
        ans += a[i][j] - min_a
print(ans)
