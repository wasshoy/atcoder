# 5.5m AC
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
ans = INF
for i in range(-100, 101):
    cost = 0
    for j in a:
        cost += (i - j) ** 2
    ans = min(ans, cost)
print(ans)
