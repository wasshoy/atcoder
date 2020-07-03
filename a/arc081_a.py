# 9m AC
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
a = LI()
a = sorted(a)[::-1]
counter = Counter(a).items()
hen4 = [elem[0] for elem in counter if elem[1] >= 4]
hen2 = [elem[0] for elem in counter if elem[1] >= 2]
if len(hen4) == 0 and len(hen2) == 0:
    print(0)
    sys.exit()

if len(hen4) > 0:
    seihoukei = hen4[0] ** 2
    if len(hen2) >= 2:
        chouhoukei = hen2[0] * hen2[1]
        ans = max(seihoukei, chouhoukei)
    else:
        ans = seihoukei
    print(ans)

else:
    print(hen2[0] * hen2[1])
