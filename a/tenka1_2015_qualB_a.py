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

res = [-1] * 20
res[0] = 100
res[1] = 100
res[2] = 200


def f(n):
    if res[n] != -1:
        return res[n]

    res[n] = f(n-1) + f(n-2) + f(n-3)
    return res[n]


print(f(19))
