import sys
import math


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


s, p = LI()
for i in range(1, int(math.sqrt(p)) + 1):
    if i*(s-i) == p:
        print('Yes')
        exit()
print('No')
