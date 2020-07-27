# 10m AC 1WA
from itertools import permutations, product
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
ans = []
l = ['a', 'b', 'c']

for elem in product(l, repeat=n):
    print(''.join(elem))