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

n = I()
a = LI()
a.sort()
ai = a[-1]
aj = a[-2]
for elem in a[:-1]:
    if abs(ai - 2*elem) < abs(ai - 2*aj):
        aj = elem
print(ai, aj)
