# 8m AC
import math
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


n, d = LI()
x = LIR(n)
ans = 0
dists = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        for l in range(1, dis + 1):
            if l ** 2 == dis:
                ans += 1
                break
print(ans)
