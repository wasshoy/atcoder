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


# 8m + 1WA AC
s = S()
d = Counter(s).keys()
if (('N' in d and 'S' in d) or ('N' not in d and 'S' not in d)) and (('W' in d and 'E' in d) or ('W' not in d and 'E' not in d)):
    print('Yes')
else:
    print('No')
