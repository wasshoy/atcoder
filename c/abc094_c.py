# 20m AC
import bisect
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
x = LI()
sx = [(i, x[i]) for i in range(n)]
sx = sorted(sx, key=lambda a: a[1])
mid_l = sx[n // 2 - 1][1]
mid_r = sx[n // 2][1]
# print(mid_l, mid_r)
sx = [(sx[i][0], i, sx[i][1]) for i in range(n)]
sx = sorted(sx, key=lambda a: a[0])
# print(sx)
for _, sort_i, elem in sx:
    if sort_i < n // 2:
        print(mid_r)
    else:
        print(mid_l)
