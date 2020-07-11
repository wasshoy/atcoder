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
a = LI()
ans = 0
for i, elem in enumerate(a):
    if (i + 1) % 2 != 0 and elem % 2 != 0:
        ans += 1
print(ans)
