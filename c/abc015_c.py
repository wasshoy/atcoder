import sys
from itertools import product


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


# 41
n, k = LI()
t = LIR(n)
for p in product(*t):
    xor_sum = 0
    for v in p:
        xor_sum ^= v
    if xor_sum == 0:
        print('Found')
        exit()
print('Nothing')
