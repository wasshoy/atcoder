# 41m AC
from collections import Counter
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


n = I()
if n % 2 != 0:
    print(0)
    exit()
ans = 0
i = 10
while i <= n:
    ans += n // i
    i *= 5
print(ans)
