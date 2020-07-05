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
d = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for _ in range(n):
    s = S()
    d[s] += 1
for k, v in d.items():
    print(f'{k} x {v}')
