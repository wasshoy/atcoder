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

# 1WA + 29m AC
n = I()
k = I()
if k == 1:
    print('YES')
    exit()

if n >= 2*k:
    print('YES')
else:
    print('NO')
