# 42m 1WA AC
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


n, s = input().split()
n = int(n)
ans = 0
for i in range(n):
    d = defaultdict(int)
    for j in range(i, n):
        if j < n:
            d[s[j]] += 1
        if d['A'] == d['T'] and d['C'] == d['G']:
            ans += 1
print(ans)
