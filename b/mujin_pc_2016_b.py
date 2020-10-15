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


# 35
l_oa, l_ab, l_bc = LI()
max_r = sum((l_oa, l_ab, l_bc))
x, y, z = sorted((l_oa, l_ab, l_bc))
min_r = 0 if x + y >= z else z - (x+y)
ans = math.pi * (max_r**2 - min_r**2)
print(ans)
