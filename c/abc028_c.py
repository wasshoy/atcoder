import sys
from itertools import combinations


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 7m+1WA AC
nums = LI()
combi = combinations(nums, 3)
sums = [sum(v) for v in combi]
sums.sort()
print(sums[-3])
