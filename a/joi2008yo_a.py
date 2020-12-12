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
# 32
pay = I()
change = 1000 - pay
ans = 0
for coin in (500, 100, 50, 10, 5, 1):
    ans += change // coin
    change %= coin
print(ans)
