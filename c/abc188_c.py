import sys


def input(): return sys.stdin.readline().strip()
def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')
MOD = 10**9 + 7


n = I()
a = LI()
l = max(a[:2**(n-1)])
r = max(a[2**(n-1):])
print(a.index(min(l, r)))
