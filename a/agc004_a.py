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

# 25
a, b, c = LI()
if a*b*c % 2 == 0:
    print(0)
else:
    ans = min(a*b, b*c, c*a)
    print(ans)
