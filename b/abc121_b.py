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


n, m, c = LI()
b = LI()
a = LIR(n)
cnt = 0
for i in range(n):
    sahen = 0
    sahen += c
    for j in range(m):
        sahen += a[i][j] * b[j]
    if sahen > 0:
        cnt += 1
print(cnt)
