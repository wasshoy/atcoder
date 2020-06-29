# 10:06 AC
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


n, k = LI()
a = LI()
c = Counter(a)
l = sorted(c.items(), key=lambda x: x[1])
types = len(l)
if types <= k:
    print(0)
    sys.exit()
ans = 0
i = 0
while types > k:
    ans += l[i][1]
    i += 1
    types -= 1
print(ans)
