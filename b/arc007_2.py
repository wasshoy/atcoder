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

# 12m AC
n, m = LI()
disk = IR(m)
case = [i for i in range(1, n+1)]
now = 0
for d in disk:
    if now == d:
        continue
    i = case.index(d)
    now, case[i] = case[i], now

print(*case, sep='\n')
