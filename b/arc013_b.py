# 56
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


c = I()
ans_n, ans_m, ans_l = 0, 0, 0
for _ in range(c):
    nml = LI()
    n, m, l = sorted(nml)[::-1]
    ans_n = max(ans_n, n)
    ans_m = max(ans_m, m)
    ans_l = max(ans_l, l)
print(ans_n * ans_m * ans_l)
