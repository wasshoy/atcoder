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
d = [LS() + [str(i)] for i in range(1, n+1)]
d = sorted(d, key=lambda x: (x[0], int(x[1])*(-1)))
for elem in d:
    print(elem[2])
