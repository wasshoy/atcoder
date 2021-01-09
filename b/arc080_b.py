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
MOD = 10**9 + 7

# 1WA + 63m AC
h, w = LI()
n = I()
a = LI()
colors = []
for k, v in enumerate(a, start=1):
    colors += [k] * v
ans = [[0] * w for _ in range(h)]
i = 0
j = 0
masu = [(i, j) if i % 2 == 0 else (i, w-j-1)
        for i in range(h) for j in range(w)]
for i, j in masu:
    c = colors.pop()
    ans[i][j] = c
for i in range(h):
    print(*ans[i])
