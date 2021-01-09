import sys
from collections import Counter


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 13m AC
n = I()
a = LI()
c = Counter(a)
ans = 0
for k in c.keys():
    ans = max(ans, c[k]+c[k+1]+c[k+2])
print(ans)
