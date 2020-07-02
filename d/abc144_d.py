import math
from math import degrees
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


a, b, x = LI()
x /= a
# 水が容器の半分より多い
if x >= a * b / 2:
    # 水のない部分の大きさ = a * (bの水がない部分 = c) / 2 より c部分が求まり tan(theta)が求められる
    tan = 2 * (a * b - x) / a ** 2
    theta = math.atan(tan)
    deg = math.degrees(theta)
# 水が容器の半分より少ない
else:
    tan = b ** 2 / (2 * x)
    theta = math.atan(tan)
    deg = math.degrees(theta)
print(deg)
