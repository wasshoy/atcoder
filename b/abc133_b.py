# 32
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
for i in range(n - 1):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        dis = math.sqrt(dis)
        if float(dis).is_integer():
            ans += 1
print(ans)
