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


a, b, k = LI()
cds = []
ans = 1
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        cds.append(i)
print(cds[-k])
