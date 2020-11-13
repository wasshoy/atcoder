from collections import defaultdict
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

# 04
n = I()
profits = defaultdict(int)
for _ in range(n):
    si = input()
    profits[si] += 1

m = I()
for _ in range(m):
    ti = input()
    profits[ti] -= 1

ans = max(0, max(profits.values()))

print(ans)
