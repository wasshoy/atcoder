from functools import reduce
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


n = I()
t = IR(n)


def lcm_base(a, b):
    return (a * b) // math.gcd(a, b)


def lcm_list(l): return reduce(lcm_base, l, 1)


ans = lcm_list(t)
print(ans)
