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


# 14
n = I()
l = 0
r = n+1
while r-l > 1:
    m = (l+r) // 2
    if m*(m+1) <= 2*(n+1):
        l = m
    else:
        r = m

print(n+1-l)
