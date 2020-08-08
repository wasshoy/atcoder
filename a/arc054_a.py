# 13m AC
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


l, x, y, s, d = LI()
y_route = y + x
y_rev = y - x
if s == d:
    print(0)
elif s < d:
    d_route = d - s
    d_rev = l - d_route
    time_route = d_route / y_route
    if y_rev > 0:
        time_rev = d_rev / y_rev
        print(min(time_route, time_rev))
    else:
        print(time_route)
else:  # s > d
    d_rev = s - d
    d_route = l - d_rev
    time_route = d_route / y_route
    if y_rev > 0:
        time_rev = d_rev / y_rev
        print(min(time_route, time_rev))
    else:
        print(time_route)
