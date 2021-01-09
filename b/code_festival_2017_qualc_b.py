import sys
from functools import reduce
from itertools import product
from operator import mul


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 10m AC
n = I()
a = LI()
ans = 0
for m in product((-1, 0, 1), repeat=n):
    b = [a[i] + m[i] for i in range(n)]
    res = reduce(mul, b)
    ans += 1 if res % 2 == 0 else 0
print(ans)
