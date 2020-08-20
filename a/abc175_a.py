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


s = S()

if s == 'RRR':
    ans = 3
elif s[:2] == 'RR' or s[1:] == 'RR':
    ans = 2
else:
    c = Counter(list(s))
    if c['R'] == 1:
        ans = 1
    elif c['S'] == 3:
        ans = 0
    else:
        ans = 1

print(ans)
