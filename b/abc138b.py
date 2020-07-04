from decimal import Decimal
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
a = LI()

bunbo = sum([Decimal(str(1 / i)) for i in a])
ans = Decimal(str(1 / bunbo))
print(float(ans))
