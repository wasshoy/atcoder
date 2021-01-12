import sys


def input(): return sys.stdin.readline().strip()
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

x, y = LI()
if x < y:
    if x+3 > y:
        print('Yes')
    else:
        print('No')
else:
    if y+3 > x:
        print('Yes')
    else:
        print('No')
