import sys
from sys import stdin

INF = float("inf")
def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
d = LI()
hp = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        hp += d[i] * d[j]
print(hp)
